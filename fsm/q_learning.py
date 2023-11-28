import random
import numpy as np
import gymnasium as gym
import grid_world


size = 5
n_obstacles = 4
env = gym.make("GridWorld-v0", render_mode="human", size=size, n_obstacles=n_obstacles)
q_table = np.zeros([size**4 * (size * size) ** n_obstacles, env.action_space.n])


def observation_to_int(obs):
    return (obs["agent"] * size * size) + obs["target"]


observation, info = env.reset()

# Hyperparameters
alpha = 0.75
gamma = 0.4
epsilon = 0.1


ok, total = 0, 0
for episode in range(1, 10001):
    observation, info = env.reset()
    obs = observation_to_int(observation)

    penalties = 0
    reward = 0
    done = False

    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[obs])

        action = action % 4

        new_observation, reward, terminated, trunkated, info = env.step(action)
        done = terminated or trunkated
        total += done
        ok += terminated
        new_obs = observation_to_int(new_observation)

        old_value = q_table[obs, action]
        next_max: float = np.max(q_table[new_obs])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[obs, action] = new_value

        if reward == -10:
            penalties += 1

        obs = new_obs

    if episode % 10 == 0:
        print("---")
        print("episode:", episode)
        print("stats:", ok, total, ok / total)
