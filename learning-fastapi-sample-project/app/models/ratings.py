"""Ratings model definition."""

from sqlalchemy import Column, ForeignKey, Numeric, UUID, String, func
from app.core.database import Base


class Ratings(Base):
    __tablename__: str = "ratings"

    rating_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    product_id: Column[UUID] = Column(
        UUID, ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    rating_value: Column[Numeric] = Column(Numeric(2, 1), nullable=True)

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
        return f"<Ratings(rating_id={self.rating_id}, product_id={self.product_id}, rating_value={self.rating_value})>"
