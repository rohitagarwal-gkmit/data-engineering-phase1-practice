"""Products model definition."""

from sqlalchemy import ForeignKey, String, Text, UUID
from sqlalchemy.sql import func
from app.core.database import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from typing import Any


class Products(Base):
    __tablename__: str = "products"

    # product_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    product_id: Mapped[Any] = mapped_column(UUID, primary_key=True, index=True)
    title: Mapped[Any] = mapped_column(String, nullable=False)
    product_link: Mapped[Any] = mapped_column(String, unique=True, nullable=False)
    upc: Mapped[Any] = mapped_column(String, unique=True, nullable=True)
    description: Mapped[Any] = mapped_column(Text, nullable=True)
    category_id: Mapped[Any] = mapped_column(
        UUID, ForeignKey("categories.category_id"), nullable=False
    )

    # Timestamps for soft deletion and record management
    created_at: Mapped[Any] = mapped_column(
        String, server_default=func.current_timestamp(), nullable=True
    )
    updated_at: Mapped[Any] = mapped_column(
        String,
        server_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
        nullable=True,
    )
    deleted_at: Mapped[Any] = mapped_column(String, nullable=True)

    # relationships
    category = relationship("Category", back_populates="products")
    ratings = relationship("Ratings", back_populates="product")
    reviews_summary = relationship("ReviewsSummary", back_populates="product")

    def soft_delete(self) -> None:
        """Soft delete the category by setting the deleted_at timestamp."""
        from datetime import datetime

        self.deleted_at = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"<Products(product_id={self.product_id}, title='{self.title}', product_link='{self.product_link}', upc='{self.upc}', description='{self.description}', category_id={self.category_id}, created_at={self.created_at})>"
