import grid_world
import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

load = True
size = 7
n_obstacles = 2
n_episodes = 10000

# Parallel environments
vec_env = make_vec_env(
    "GridWorld-v0",
    n_envs=1,
    env_kwargs={"render_mode": "human", "size": size, "n_obstacles": n_obstacles},
)

if load:
    model = PPO.load("ppo_grid_world.zip", vec_env)
else:
    model = PPO("MultiInputPolicy", vec_env, verbose=1)

model.learn(total_timesteps=n_episodes * 40)

model.save("ppo_grid_world")

obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")
