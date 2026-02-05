"""Ratings model definition."""

from sqlalchemy import Column, ForeignKey, Numeric, UUID
from app.core.database import Base


class Ratings(Base):
    __tablename__: str = "ratings"

    rating_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    product_id: Column[UUID] = Column(
        UUID, ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False
    )
    rating_value: Column[Numeric] = Column(Numeric(2, 1), nullable=True)

    def __repr__(self) -> str:
        return f"<Ratings(rating_id={self.rating_id}, product_id={self.product_id}, rating_value={self.rating_value})>"
