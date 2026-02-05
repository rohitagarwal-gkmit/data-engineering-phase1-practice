"""Product model definition."""

from sqlalchemy import UUID, String, Text, ForeignKey, func
from app.core.database import Base
from sqlalchemy.orm import mapped_column, relationship, Mapped


class Product(Base):
    __tablename__: str = "products"

    product_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    product_link: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    upc: Mapped[str] = mapped_column(String, unique=True, nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    category_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("categories.category_id"), nullable=False
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
    category = relationship("Category", back_populates="products")
    ratings = relationship("Ratings", back_populates="product")
    reviews_summary = relationship("ReviewsSummary", back_populates="product")

    # Soft delete method
    def soft_delete(self) -> None:
        """Soft delete the category by setting the deleted_at timestamp."""
        from datetime import datetime

        self.deleted_at = datetime.utcnow().isoformat()

    def __repr__(self) -> str:
        return f"<Product(product_id={self.product_id}, title='{self.title}', product_link='{self.product_link}')>"
