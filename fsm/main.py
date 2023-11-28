import gymnasium as gym
import fsm_labs

env = gym.make("fsm_labs/GridWorld-v0", render_mode="human")

observation, info = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    observation, reward, terminated, trunkated, info = env.step(action)

    if terminated or trunkated:
        observation, info = env.reset()

env.close()
