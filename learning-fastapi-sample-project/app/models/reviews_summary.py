"""ReviewsSummary model definition."""

from sqlalchemy import Column, ForeignKey, Integer, UUID, String, func
from app.core.database import Base


class ReviewsSummary(Base):
    __tablename__: str = "reviews_summary"

    review_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    product_id: Column[UUID] = Column(
        UUID, ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    number_of_reviews: Column[int] = Column(Integer, nullable=True)

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
        return f"<ReviewsSummary(review_id={self.review_id}, product_id={self.product_id}, number_of_reviews={self.number_of_reviews})>"
