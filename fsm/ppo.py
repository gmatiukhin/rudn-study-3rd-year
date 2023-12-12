import grid_world
import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

size = 5
n_obstacles = 1

# Parallel environments
vec_env = make_vec_env("GridWorld-v0", n_envs=2, env_kwargs={"render_mode": "human", "size": size, "n_obstacles": n_obstacles})
print(vec_env.reset())

model = PPO("MultiInputPolicy", vec_env, verbose=1)
model.learn(total_timesteps=25000)

obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")
