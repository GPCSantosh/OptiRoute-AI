from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db


async def get_database(
    db: AsyncSession = Depends(get_db),
):
    return db