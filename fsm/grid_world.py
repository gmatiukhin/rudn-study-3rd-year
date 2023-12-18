from itertools import pairwise
import numpy as np
import pygame

import gymnasium as gym
from gymnasium import spaces
from gymnasium.envs.registration import register


class GridWorldEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self, render_mode=None, size=5, n_obstacles=2):
        self.target_tick = True
        self.size = size  # The size of the square grid
        self.window_size = 512  # The size of the PyGame window
        self.n_obstacles = n_obstacles

        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, size - 1, shape=(2,), dtype=np.int64),
                "target": spaces.Box(0, size - 1, shape=(2,), dtype=np.int64),
                "obstacles": spaces.MultiDiscrete(
                    np.array([size - 1 for _ in range(2 * n_obstacles)]), dtype=np.int64
                ),
            }
        )

        # We have 4 actions, corresponding to "right", "up", "left", "down"
        self.action_space = spaces.Discrete(4)

        """
        The following dictionary maps abstract actions from `self.action_space` to
        the direction we will walk in if that action is taken.
        I.e. 0 corresponds to "right", 1 to "up" etc.
        """
        self._action_to_direction = {
            0: np.array([1, 0]),  # right
            1: np.array([0, 1]),  # up
            2: np.array([-1, 0]),  # left
            3: np.array([0, -1]),  # bottom
        }

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

        """
        If human-rendering is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None

    def _get_obs(self):
        return {
            "agent": self._agent_location,
            "target": self._target_location,
            "obstacles": self._obstacles_locations.flatten(),
        }

    def _get_info(self):
        return {
            "distance": np.linalg.norm(
                self._agent_location - self._target_location, ord=1
            )
        }

    def reset(self, seed=None, options=None):
        # We need the following line to seed self.np_random
        super().reset(seed=seed)

        # Choose the agent's location uniformly at random

        taken_locations = []
        obstacles_locations = []
        sample = self.observation_space["obstacles"].sample()
        for i, (x, y) in enumerate(pairwise(sample)):
            if i % 2 == 1:
                continue
            o = np.array([x, y])
            obstacles_locations.append(o)
            taken_locations.append(o)
        self._obstacles_locations = np.array(obstacles_locations)

        while True:
            self._agent_location = self.np_random.integers(
                0, self.size, size=2, dtype=int
            )
            agent_is_unique = True
            for t in taken_locations:
                agent_is_unique = agent_is_unique and not np.array_equal(
                    self._agent_location, t
                )
            if agent_is_unique:
                break
        taken_locations.append(self._agent_location)

        while True:
            self._target_location = self.np_random.integers(
                0, self.size, size=2, dtype=int
            )
            target_is_unique = True
            for t in taken_locations:
                target_is_unique = target_is_unique and not np.array_equal(
                    self._target_location, t
                )
            if target_is_unique:
                break

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, info

    def step(self, action):
        self.target_tick = not self.target_tick
        if self.target_tick == True:
            self._target_location[0] += 1
            self._target_location[0] %= self.size
        # Map the action (element of {0,1,2,3}) to the direction we walk in
        old_distance = np.linalg.norm(self._agent_location - self._target_location)
        old_location = self._agent_location
        direction = self._action_to_direction[action]
        # We use `np.clip` to make sure we don't leave the grid
        self._agent_location = np.clip(
            self._agent_location + direction, 0, self.size - 1
        )
        new_distance = np.linalg.norm(self._agent_location - self._target_location)
        # An episode is done iff the agent has reached the target
        terminated = np.array_equal(self._agent_location, self._target_location)
        reward = old_distance - new_distance

        # Don't stay in the same place, dummy
        if np.array_equal(old_location, self._agent_location):
            reward -= 5

        # Don't move into obstacles
        for o in self._obstacles_locations:
            if np.array_equal(self._agent_location, o):
                reward -= 5
                self._agent_location = old_location
                break

        observation = self._get_obs()
        info = self._get_info()

        if self.render_mode == "human":
            self._render_frame()

        return observation, reward, terminated, False, info

    def render(self):
        if self.render_mode == "rgb_array":
            return self._render_frame()

    def _render_frame(self):
        if self.window is None and self.render_mode == "human":
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
        if self.clock is None and self.render_mode == "human":
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((255, 255, 255))
        pix_square_size = (
            self.window_size / self.size
        )  # The size of a single grid square in pixels

        # Draw obstacles
        for o in self._obstacles_locations:
            pygame.draw.rect(
                canvas,
                (40, 40, 40),
                pygame.Rect(
                    pix_square_size * o,
                    (pix_square_size, pix_square_size),
                ),
            )

        # First we draw the target
        pygame.draw.rect(
            canvas,
            (255, 0, 0),
            pygame.Rect(
                pix_square_size * self._target_location,
                (pix_square_size, pix_square_size),
            ),
        )
        # Now we draw the agent
        pygame.draw.circle(
            canvas,
            (0, 0, 255),
            (self._agent_location + 0.5) * pix_square_size,
            pix_square_size / 3,
        )

        # Finally, add some gridlines
        for x in range(self.size + 1):
            pygame.draw.line(
                canvas,
                0,
                (0, pix_square_size * x),
                (self.window_size, pix_square_size * x),
                width=3,
            )
            pygame.draw.line(
                canvas,
                0,
                (pix_square_size * x, 0),
                (pix_square_size * x, self.window_size),
                width=3,
            )

        if self.render_mode == "human":
            # The following line copies our drawings from `canvas` to the visible window
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()

            # We need to ensure that human-rendering occurs at the predefined framerate.
            # The following line will automatically add a delay to keep the framerate stable.
            self.clock.tick(self.metadata["render_fps"])
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )

    def close(self):
        if self.window is not None:
            pygame.display.quit()
            pygame.quit()


register(
    id="GridWorld-v0",
    entry_point="grid_world:GridWorldEnv",
    max_episode_steps=40,
)
