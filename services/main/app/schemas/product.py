from pydantic import BaseModel, Field, UUID4, validator
from decimal import Decimal
from datetime import datetime

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    price: Decimal = Field(..., gt=0)

class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = None
    price: Decimal | None = Field(None, gt=0)

class ProductResponse(BaseModel):
    id: UUID4
    name: str
    description: str | None
    price: Decimal
    created_by: UUID4
    created_at: datetime
    updated_at: datetime | None
