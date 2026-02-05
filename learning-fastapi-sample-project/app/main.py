from fastapi import FastAPI
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.core.database import get_db
from sqlalchemy.sql import text

app = FastAPI()


@app.get(path="/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get(path="/database-health")
async def database_health_check() -> dict[str, str]:

    db: AsyncSession = (
        await get_db().__anext__()
    )  # Get the first item from the async generator

    try:
        await db.execute(text("SELECT 1"))
        return {"database_status": "ok"}
    except Exception as e:
        return {"database_status": "error", "details": str(e)}
    finally:
        await db.close()
