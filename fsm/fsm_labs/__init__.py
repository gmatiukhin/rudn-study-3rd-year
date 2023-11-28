from gymnasium.envs.registration import register

register(
    id="fsm_labs/GridWorld-v0",
    entry_point="fsm_labs.envs:GridWorldEnv",
    max_episode_steps=300,
)
