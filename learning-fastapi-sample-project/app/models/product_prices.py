"""ProductPrices model definition."""

from sqlalchemy import Column, ForeignKey, Numeric, String, TIMESTAMP, UUID
from sqlalchemy.sql import func
from app.core.database import Base


class ProductPrices(Base):
    __tablename__: str = "product_prices"

    price_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    product_id: Column[UUID] = Column(
        UUID, ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    price_excl_tax: Column[Numeric] = Column(Numeric(10, 2), nullable=True)
    price_incl_tax: Column[Numeric] = Column(Numeric(10, 2), nullable=True)
    tax: Column[Numeric] = Column(Numeric(10, 2), nullable=True)
    currency: Column[str] = Column(String(3), default="GBP", nullable=True)
    effective_from: Column[TIMESTAMP] = Column(
        TIMESTAMP, server_default=func.current_timestamp(), nullable=True
    )

    def __repr__(self) -> str:
        return f"<ProductPrices(price_id={self.price_id}, product_id={self.product_id}, price_excl_tax={self.price_excl_tax}, price_incl_tax={self.price_incl_tax}, tax={self.tax}, currency='{self.currency}', effective_from={self.effective_from})>"
