import logging
import os
import sys
from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings, AnyUrl

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    """Base Settings"""

    environment: str = os.getenv("ENVIRONMENT", "dev")

    """Database configurations"""
    # database_url: AnyUrl = get_database_url()
    # database_name: str = "fast-geo"
    # database_user: str = os.getenv("ARANGO_USER", "root")
    # database_password: str = os.getenv("ARANGO_PWD", "openSesame")
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
