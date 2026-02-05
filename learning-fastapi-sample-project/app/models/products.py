"""Products model definition."""

from sqlalchemy import Column, ForeignKey, String, Text, TIMESTAMP, UUID
from sqlalchemy.sql import func
from app.core.database import Base


class Products(Base):
    __tablename__: str = "products"

    product_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    title: Column[str] = Column(String, nullable=False)
    product_link: Column[str] = Column(String, unique=True, nullable=False)
    upc: Column[str] = Column(String, unique=True, nullable=True)
    description: Column[str] = Column(Text, nullable=True)
    category_id: Column[UUID] = Column(
        UUID, ForeignKey("categories.category_id"), nullable=False
    )
    created_at: Column[TIMESTAMP] = Column(
        TIMESTAMP, server_default=func.current_timestamp(), nullable=True
    )

    def __repr__(self) -> str:
        return f"<Products(product_id={self.product_id}, title='{self.title}', product_link='{self.product_link}', upc='{self.upc}', description='{self.description}', category_id={self.category_id}, created_at={self.created_at})>"
