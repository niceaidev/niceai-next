import os

import dotenv

dotenv.load_dotenv()

DEFAULTS = {
    'DATABASE_URL': '',
    'APP_NAME': 'Nice AI',
    'TABLE_PREFIX': 'na_',
}


def get_env(key):
    return os.environ.get(key, DEFAULTS.get(key))


def get_bool_env(key):
    value = get_env(key)
    return value.lower() == 'true' if value is not None else False


def get_cors_allow_origins(env, default):
    cors_allow_origins = []
    if get_env(env):
        for origin in get_env(env).split(','):
            cors_allow_origins.append(origin)
    else:
        cors_allow_origins = [default]

    return cors_allow_origins


class Config:
    """Application configuration class."""

    def __init__(self):
        # ------------------------
        # General Configurations.
        # ------------------------
        self.CURRENT_VERSION = "0.6.9"
        self.DATABASE_URL = get_env('DATABASE_URL')
        self.APP_NAME = get_env('APP_NAME')


config = Config()
