from functools import lru_cache
from pydantic import BaseSettings

class DataBaseSettings(BaseSettings):
    """
    """
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_schema: str = ''

@lru_cache
def get_db_settings() -> BaseSettings:
    """
    """
    return DataBaseSettings()
