import pytest
from sqlalchemy import select
from config.Database import DATABASE_URL, Db
from depends import tron_scan_service
from schemas.TronScan import TronScan


@pytest.mark.asyncio
async def test_create_scan_in_db():
    test_address = "TR7NHqjeKQxGTCi8q8ZY4pL8ot"
    db = Db(DATABASE_URL)

    async for session in db.session_getter():
        await tron_scan_service.create_scan(session, test_address)

        result = await session.execute(
            select(TronScan).where(TronScan.address == test_address)
        )
        db_record = result.scalar_one()

        assert db_record is not None
        assert db_record.address == test_address
