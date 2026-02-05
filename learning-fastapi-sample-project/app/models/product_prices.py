"""ProductPrices model definition."""

from sqlalchemy import ForeignKey, Numeric, String, TIMESTAMP, UUID
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped


class ProductPrices(Base):
    __tablename__: str = "product_prices"

    price_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    product_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    price_excl_tax: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=True)
    price_incl_tax: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=True)
    tax: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=True)
    currency: Mapped[str] = mapped_column(String(3), default="GBP", nullable=True)
    effective_from: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, server_default=func.current_timestamp(), nullable=True
    )

    # Timestamps for soft deletion and record management
    created_at: Mapped[str] = mapped_column(
        String, server_default=func.current_timestamp(), nullable=True
    )
    updated_at: Mapped[str] = mapped_column(
        String,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=True,
    )
    deleted_at: Mapped[str] = mapped_column(String, nullable=True)

    # relationships
    product = relationship("Product", back_populates="prices")

    # Soft delete method
    def soft_delete(self) -> None:
        """Soft delete the category by setting the deleted_at timestamp."""
        from datetime import datetime

        self.deleted_at = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"<ProductPrices(price_id={self.price_id}, product_id={self.product_id}, price_excl_tax={self.price_excl_tax}, price_incl_tax={self.price_incl_tax}, tax={self.tax}, currency='{self.currency}', effective_from={self.effective_from})>"
