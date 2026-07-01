from collections.abc import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings
from app.core.logger import logger

# -------------------------------------------------------------------
# Convert PostgreSQL URL to asyncpg URL if necessary
# -------------------------------------------------------------------

DATABASE_URL = settings.DATABASE_URL

if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+asyncpg://",
        1,
    )

# -------------------------------------------------------------------
# Async SQLAlchemy Engine
# -------------------------------------------------------------------

engine = create_async_engine(
    DATABASE_URL,
    echo=settings.DEBUG,
    future=True,
    pool_pre_ping=True,
    pool_size=20,
    max_overflow=10,
    pool_recycle=1800,
)

# -------------------------------------------------------------------
# Session Factory
# -------------------------------------------------------------------

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)

# -------------------------------------------------------------------
# FastAPI Dependency
# -------------------------------------------------------------------

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency used in API routes.

    Example:

        @router.get("/")
        async def get_items(
            db: AsyncSession = Depends(get_db)
        ):
            ...
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session

        except Exception:
            await session.rollback()
            raise

        finally:
            await session.close()

# -------------------------------------------------------------------
# Database Health Check
# -------------------------------------------------------------------

async def check_database_connection() -> bool:
    """
    Returns True if PostgreSQL is reachable.
    """

    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))

        logger.bind(module="database").success(
            "Database connection established."
        )

        return True

    except Exception as exc:
        logger.bind(module="database").exception(exc)
        return False

# -------------------------------------------------------------------
# Graceful Shutdown
# -------------------------------------------------------------------

async def close_database() -> None:
    """
    Dispose SQLAlchemy connection pool.
    """

    logger.bind(module="database").info(
        "Closing database connections..."
    )

    await engine.dispose()

    logger.bind(module="database").success(
        "Database connections closed."
    )