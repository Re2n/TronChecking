from functools import lru_cache
import os

from pydantic_settings import BaseSettings


@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    APP_PORT: int
    API_KEY_TRONGRID: str

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
