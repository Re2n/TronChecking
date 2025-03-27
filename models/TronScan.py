import decimal
from datetime import datetime

from pydantic import BaseModel


class TronScan(BaseModel):
    id: int
    address: str
    created_at: datetime

    class Config:
        from_attributes = True

class TronScanResponse(BaseModel):
    address: str
    balance: decimal.Decimal
    bandwidth: int
    energy: str
