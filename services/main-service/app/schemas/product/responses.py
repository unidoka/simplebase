from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.schemas.user.response import UserResponse
from app.schemas.pagination.const import Pagination


class ProductResponse(BaseModel):
    id: UUID

    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = None

    creator: UserResponse

    class Config:
        from_attributes = True

    created_at: datetime
    updated_at: datetime

class ProductListResponse(BaseModel):
    items: list[ProductResponse]
    paginate: Pagination