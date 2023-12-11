import random
import numpy as np
import gymnasium as gym
import grid_world


size = 5
n_obstacles = 1
n_episodes = 10000

env = gym.make("GridWorld-v0", render_mode=None, size=size, n_obstacles=n_obstacles)
shape = [size**2, size**2]
for _ in range(n_obstacles):
    shape.append(size**2)
shape.append(env.action_space.n)
q_table = np.zeros(shape)


def observation_to_idx(obs):
    agent_idx = obs["agent"][0] * size + obs["agent"][1]
    target_idx = obs["target"][0] * size + obs["target"][1]
    idxs = []
    for o in obs["obstacles"]:
        idxs.append(o[0] * size + o[1])
    return [agent_idx, target_idx, *idxs]


observation, info = env.reset()

# Hyperparameters
alpha = 0.75
gamma = 0.4
epsilon = 0.1


ok, total = 0, 0
for episode in range(1, n_episodes + 1):
    observation, info = env.reset()
    obs = observation_to_idx(observation)

    penalties = 0
    reward = 0
    done = False

    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[*obs])

        new_observation, reward, terminated, trunkated, info = env.step(action)
        done = terminated or trunkated
        total += done
        ok += terminated
        new_obs = observation_to_idx(new_observation)

        old_value = q_table[*obs, action]
        next_max: float = np.max(q_table[*new_obs])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[*obs, action] = new_value

        if reward == -10:
            penalties += 1

        obs = new_obs

    if episode % 1000 == 0:
        print("---")
        print("episode:", episode)
        print("stats:", ok, total, ok / total)
