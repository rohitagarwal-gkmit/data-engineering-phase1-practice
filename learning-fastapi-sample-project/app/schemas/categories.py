"""
Schemas for categories.
"""

from pydantic import BaseModel


class CategoryBase(BaseModel):
    """Base schema for category."""

    name: str


class CategoryResponse(CategoryBase):
    """Schema for category response."""

    category_id: str

    class Config:
        orm_mode = True


class CategoryListResponse(BaseModel):
    """Schema for category list response."""

    categories: list[CategoryResponse]

    class Config:
        orm_mode = True


class CategoryCreateRequest(CategoryBase):
    """Schema for category creation request."""

    pass


class CategoryCreateResponse(CategoryResponse):
    """Schema for category creation response."""

    message: str
    pass


class CategoryUpdateRequest(CategoryBase):
    """Schema for category update request."""

    name: str | None = None


class CategoryUpdateResponse(CategoryResponse):
    """Schema for category update response."""

    message: str


class CategoryDeleteRequest(BaseModel):
    """Schema for category delete request."""

    category_id: str


class CategoryDeleteResponse(BaseModel):
    """Schema for category delete response."""

    message: str
