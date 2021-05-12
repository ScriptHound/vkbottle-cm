from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from config.db_config import engine

# at the module level, the global sessionmaker,
# bound to a specific Engine
AsyncSession = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class DBAdapter:
    @asynccontextmanager
    async def get_session(self):
        session = AsyncSession()
        try:
            yield session
            await session.commit()
        except Exception:  # NOQA
            await session.rollback()
            raise
        finally:
            await session.close()
