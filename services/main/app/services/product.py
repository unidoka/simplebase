from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID
from ..models.user import User
from ..models.product import Product
from ..schemas.product import ProductCreate, ProductUpdate

async def create_product(db: AsyncSession, user: User, data: ProductCreate):
    # TODO: создать товар
    pass

async def get_product(db: AsyncSession, product_id: UUID):
    # TODO: получить товар, 404 если нет
    pass

async def update_product(db: AsyncSession, product_id: UUID, user: User, data: ProductUpdate):
    # TODO: обновить, проверить владельца
    pass

async def delete_product(db: AsyncSession, product_id: UUID, user: User):
    # TODO: удалить, проверить владельца
    pass

async def list_products(db: AsyncSession, skip: int = 0, limit: int = 10, sort: str = "created_at"):
    # TODO: пагинация и сортировка
    pass
