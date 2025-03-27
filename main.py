from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from config.Database import db
from depends import tron_scan_service
from routers.TronScan import tron_scan_router
from schemas.Base import Base

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await db.dispose()
    await tron_scan_service.close_tron()


app.include_router(tron_scan_router)
add_pagination(app)