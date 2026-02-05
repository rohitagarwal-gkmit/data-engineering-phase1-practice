"""ProductInventory model definition."""

from sqlalchemy import Column, UUID, Integer, ForeignKey, String, func
from app.core.database import Base


class ProductInventory(Base):
    __tablename__: str = "product_inventory"

    inventory_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    product_id: Column[UUID] = Column(
        UUID, ForeignKey("products.product_id"), nullable=False
    )
    availability_status: Column[str] = Column(
        String, nullable=False
    )  # e.g., 'in_stock', 'out_of_stock'
    availability_count: Column[int] = Column(Integer, nullable=True)

    # Timestamps for soft deletion and record management
    created_at: Column[str] = Column(
        String, server_default=func.current_timestamp(), nullable=True
    )
    updated_at: Column[str] = Column(
        String,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=True,
    )
    deleted_at: Column[str] = Column(String, nullable=True)

    def soft_delete(self) -> None:
        """Soft delete the category by setting the deleted_at timestamp."""
        from datetime import datetime

        self.deleted_at = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"<ProductInventory(inventory_id={self.inventory_id}, product_id={self.product_id}, availability_status='{self.availability_status}', availability_count={self.availability_count})>"
