from sqlalchemy.ext.asyncio import AsyncSession

from app.models.model_score import Scores

async def create_score(db: AsyncSession, item: Scores):
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item
