from sqlalchemy.ext.asyncio import AsyncSession

from schemas.TronScan import TronScan


class TronScanRepository:
    model = TronScan

    async def create_scan(self, session: AsyncSession, address: str):
        new_scan = self.model(address=address)
        session.add(new_scan)
        await session.commit()
        return new_scan
