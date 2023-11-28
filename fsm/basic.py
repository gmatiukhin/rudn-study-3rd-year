import gymnasium as gym
import grid_world


env = gym.make("GridWorld-v0", render_mode="human")

observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, trunkated, info = env.step(action)

    if terminated or trunkated:
        observation, info = env.reset()

env.close()
