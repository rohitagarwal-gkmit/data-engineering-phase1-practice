"""Product model definition."""

from sqlalchemy import Column, UUID, String, Text, ForeignKey, TIMESTAMP
from app.core.database import Base


class Product(Base):
    __tablename__: str = "products"

    product_id: Column[UUID] = Column(UUID, primary_key=True, index=True)
    title: Column[str] = Column(String, nullable=False)
    product_link: Column[str] = Column(String, unique=True, nullable=False)
    upc: Column[str] = Column(String, unique=True, nullable=True)
    description: Column[str] = Column(Text, nullable=True)
    category_id: Column[UUID] = Column(
        UUID, ForeignKey("categories.category_id"), nullable=False
    )
    created_at: Column[str] = Column(
        TIMESTAMP, server_default="CURRENT_TIMESTAMP", nullable=True
    )

    def __repr__(self) -> str:
        return f"<Product(product_id={self.product_id}, title='{self.title}', product_link='{self.product_link}')>"
