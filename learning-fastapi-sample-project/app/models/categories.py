"""
Category model definition.
"""

from sqlalchemy import UUID, Column, String, func
from app.core.database import Base


class Category(Base):
    __tablename__: str = "categories"

    category_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    category_name: Column[str] = Column(String, unique=True, nullable=False)

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

    # Representation method for debugging purposes
    def __repr__(self) -> str:
        return f"<Category(category_id={self.category_id}, category_name='{self.category_name}')>"
