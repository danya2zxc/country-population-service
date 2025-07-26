from sqlalchemy import MetaData, NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import config

engine = create_async_engine(config.database_url, poolclass=NullPool, echo=True)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
metadata = MetaData()


class Base(DeclarativeBase):
    """
    Base class for all models.
    """

    metadata = metadata
    pass
