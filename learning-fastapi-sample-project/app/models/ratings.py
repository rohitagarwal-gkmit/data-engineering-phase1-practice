"""Ratings model definition."""

from sqlalchemy import ForeignKey, Numeric, UUID, String, func
from app.core.database import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped


class Ratings(Base):
    __tablename__: str = "ratings"

    rating_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    product_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    rating_value: Mapped[Numeric] = mapped_column(Numeric(2, 1), nullable=True)

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
    product = relationship("Products", back_populates="ratings")

    # Soft delete method
    def soft_delete(self) -> None:
        """Soft delete the category by setting the deleted_at timestamp."""
        from datetime import datetime

        self.deleted_at = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"<Ratings(rating_id={self.rating_id}, product_id={self.product_id}, rating_value={self.rating_value})>"
