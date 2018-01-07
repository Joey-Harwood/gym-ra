from gym.envs.registration import register

register(
    id='ra-v0',
    entry_point='gym_ra.envs:RaEnv',
)
register(
    id='ra-extrahard-v0',
    entry_point='gym_ra.envs:RaExtraHardEnv',
)