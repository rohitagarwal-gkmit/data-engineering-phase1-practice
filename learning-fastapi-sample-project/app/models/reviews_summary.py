"""ReviewsSummary model definition."""

from sqlalchemy import ForeignKey, Integer, UUID, String, func
from app.core.database import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped


class ReviewsSummary(Base):
    __tablename__: str = "reviews_summary"

    review_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    product_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    number_of_reviews: Mapped[int] = mapped_column(Integer, nullable=True)
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
    product = relationship("Product", back_populates="reviews_summary")

    # Soft delete method
    def soft_delete(self) -> None:
        """Soft delete the category by setting the deleted_at timestamp."""
        from datetime import datetime

        self.deleted_at = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"<ReviewsSummary(review_id={self.review_id}, product_id={self.product_id}, number_of_reviews={self.number_of_reviews})>"
