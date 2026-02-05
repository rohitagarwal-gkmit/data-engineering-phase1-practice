"""ReviewsSummary model definition."""

from sqlalchemy import Column, ForeignKey, Integer, UUID
from app.core.database import Base


class ReviewsSummary(Base):
    __tablename__: str = "reviews_summary"

    review_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    product_id: Column[UUID] = Column(
        UUID, ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    number_of_reviews: Column[int] = Column(Integer, nullable=True)

    def __repr__(self) -> str:
        return f"<ReviewsSummary(review_id={self.review_id}, product_id={self.product_id}, number_of_reviews={self.number_of_reviews})>"
