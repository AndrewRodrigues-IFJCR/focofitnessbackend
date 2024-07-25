from datetime import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, autoincrement=True)
    create_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    update_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now
    )
