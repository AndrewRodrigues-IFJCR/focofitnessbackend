from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Account(Base):
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column()
