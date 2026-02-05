"""
Category model definition.
"""

from sqlalchemy import UUID, String, func
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.core.database import Base


class Category(Base):
    __tablename__: str = "categories"

    category_id: Mapped[UUID] = mapped_column(UUID, primary_key=True, index=True)
    category_name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

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
    products = relationship("Product", back_populates="category")

    # Soft delete method
    def soft_delete(self) -> None:
        """Soft delete the category by setting the deleted_at timestamp."""
        from datetime import datetime

        self.deleted_at = datetime.utcnow().isoformat()

    # Representation method for debugging purposes
    def __repr__(self) -> str:
        return f"<Category(category_id={self.category_id}, category_name='{self.category_name}')>"
