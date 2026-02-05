"""ProductInventory model definition."""

from sqlalchemy import UUID, Integer, ForeignKey, String, func
from app.core.database import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped


class ProductInventory(Base):
    __tablename__: str = "product_inventory"

    inventory_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    product_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("products.product_id"), nullable=False
    )
    availability_status: Mapped[str] = mapped_column(
        String, nullable=False
    )  # e.g., 'in_stock', 'out_of_stock'
    availability_count: Mapped[int] = mapped_column(Integer, nullable=True)

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
    product = relationship("Product", back_populates="inventory")

    # Soft delete method
    def soft_delete(self) -> None:
        """Soft delete the category by setting the deleted_at timestamp."""
        from datetime import datetime

        self.deleted_at = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"<ProductInventory(inventory_id={self.inventory_id}, product_id={self.product_id}, availability_status='{self.availability_status}', availability_count={self.availability_count})>"
