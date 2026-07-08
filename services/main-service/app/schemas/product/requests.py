from pydantic import BaseModel
from decimal import Decimal

class CreateProduct(BaseModel):

    name: str
    description: str | None = None
    price: Decimal


class UpdateProduct(BaseModel):

    name: str | None = None
    description: str | None = None
    price: Decimal | None = None