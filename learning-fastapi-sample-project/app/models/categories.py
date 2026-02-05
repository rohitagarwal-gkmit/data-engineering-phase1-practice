"""
Category model definition.
"""

from sqlalchemy import UUID, Column, String
from app.core.database import Base


class Category(Base):
    __tablename__: str = "categories"

    category_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    category_name: Column[str] = Column(String, unique=True, nullable=False)

    # Representation method for debugging purposes
    def __repr__(self) -> str:
        return f"<Category(category_id={self.category_id}, category_name='{self.category_name}')>"
