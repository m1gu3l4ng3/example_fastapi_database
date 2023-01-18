from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

from app.config.db_settings import get_db_settings

settings_db = get_db_settings()

SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{quote_plus(settings_db.postgres_user)}:"
    f"{quote_plus(settings_db.postgres_password)}@"
    f"{quote_plus(settings_db.postgres_host)}/"
    f"{quote_plus(settings_db.postgres_db)}"
)
   

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=True,
    connect_args = {
        'ssl': False
    }
)

Base = declarative_base(metadata=MetaData(schema=settings_db.postgres_schema))
