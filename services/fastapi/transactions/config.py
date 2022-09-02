import logging
import os
import sys
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Base Settings"""

    environment: str = os.getenv("ENVIRONMENT", "dev")

    """Database configurations"""
    database_name: str = os.getenv("POSTGRES_DB")
    database_user: str = os.getenv("POSTGRES_USER")
    database_password: str = os.getenv("POSTGRES_PASSWORD")
    database_host: str = os.getenv("POSTGRES_HOST")
    database_url: AnyUrl = f"postgresql://{database_user}:{database_password}@{database_host}/{database_name}"
    """Testing configurations"""
    testing: bool = "unittest" in sys.modules.keys()
    test_database_name: str = "testdb"

    """External services configurations"""
    users_service_base_url: str = os.getenv(
        "USERS_SERVICE_BASE_URL", "http://localhost:8000"
    )
    rabbit_url: str = os.getenv(
        "RABBITMQ_URL_STRING", "amqp://R063r:r4B8170@localhost:5672/"
    )


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
