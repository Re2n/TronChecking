from sqlalchemy.ext.asyncio import AsyncSession
from tronpy import AsyncTron
from tronpy.providers import AsyncHTTPProvider

from models.TronScan import TronScanResponse
from repositories.TronScan import TronScanRepository

class TronScanService:
    def __init__(
        self,
        tron_scan_repository: TronScanRepository,
        provider: AsyncHTTPProvider,
    ):
        self.repository = tron_scan_repository
        self.provider = provider
        self.tron = None

    async def create_scan(
        self,
        session: AsyncSession,
        address: str,
    ):
        new_scan = await self.repository.create_scan(session, address)
        return new_scan

    async def get_info_about_address(self, address: str):
        self.tron = AsyncTron(provider=self.provider)
        await self.tron.__aenter__()
        balance = await self.tron.get_account_balance(address)
        bandwidth = await self.tron.get_bandwidth(address)
        resources = await self.tron.get_account_resource(address)
        energy_used = resources.get("EnergyUsed")
        energy_limit = resources.get("EnergyLimit")
        if energy_limit is None:
            return TronScanResponse(
                address=address,
                balance=balance,
                bandwidth=bandwidth,
                energy="0/0",
            )
        return TronScanResponse(
            address=address,
            balance=balance,
            bandwidth=bandwidth,
            energy=f"{energy_limit-energy_used}/{energy_limit}",
        )

    async def close_tron(self):
        if self.tron:
            await self.tron.__aexit__(None, None, None)