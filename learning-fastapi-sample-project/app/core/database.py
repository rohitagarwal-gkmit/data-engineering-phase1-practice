from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
from sqlalchemy.orm import sessionmaker
from config.dev import DATABASE_URL


engine: AsyncEngine = create_async_engine(
    url=DATABASE_URL,
    pool_size=10,  # Initial pool size
    max_overflow=20,  # Allow overflow for bursts
    pool_timeout=30,  # Timeout for acquiring connections
    pool_recycle=3600,  # Recycle connections every hour
    echo=False,  # Set to True for debugging
)

AsyncSessionLocal: sessionmaker[AsyncSession] = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
