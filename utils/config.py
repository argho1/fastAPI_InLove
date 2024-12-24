import os

from logging import getLogger

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)



logger = getLogger(__name__)

ENV_FILE_NAME = os.getenv("CONFIG_ENV_FILE", ".env")


class _Settings(BaseSettings):
    """
    The settings are loaded from environment variables from a .env file
    All values in .env must be defined as fields here
    Uses pydantic for validation
    """

    model_config = SettingsConfigDict(
        env_file = ENV_FILE_NAME, env_prefix="", extra="ignore"
    )
    # NOTE: making use of env_prefix, we can combine settings for all services in a single .env file

    DATABASE_URL: str






Config = _Settings()