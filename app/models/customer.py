from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )
    
    category: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    address: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    opening_balance: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )
    
