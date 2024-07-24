from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

ASYNC_ENGINE = create_async_engine()


def get_async_session_maker() -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(ASYNC_ENGINE)
