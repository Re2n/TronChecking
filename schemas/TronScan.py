import decimal

from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from schemas.Base import Base
from schemas.mixins.int_id_pk import IntIdPkMixin


class TronScan(IntIdPkMixin, Base):
    __tablename__ = "tronscan"

    address: Mapped[str] = mapped_column(nullable=False)
