import asyncio
from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi_pagination import Page, Params
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.Database import db
from depends import tron_scan_service
from models.TronScan import TronScanResponse
from fastapi_pagination.ext.sqlalchemy import paginate

from models.TronScan import TronScan
from schemas.TronScan import TronScan as TronScanSchema

tron_scan_router = APIRouter(tags=["Tron Scan"])


@tron_scan_router.post("/scan/{address}")
async def scan_address(
    address: str, session: Annotated[AsyncSession, Depends(db.session_getter)]
) -> TronScanResponse:
    await tron_scan_service.create_scan(session, address)
    tron_scan = await tron_scan_service.get_info_about_address(address)
    return tron_scan

@tron_scan_router.get("/get_all_scans")
async def get_all_scans(
        session: Annotated[AsyncSession, Depends(db.session_getter)],
        params: Params = Depends()
) -> Page[TronScan]:
    return await paginate(session, select(TronScanSchema), params)