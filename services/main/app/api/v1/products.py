from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from ...core.database import get_db
from ...core.security import get_current_user
from ...models.user import User
from ...schemas.product import ProductCreate, ProductUpdate, ProductResponse
from ...services import product as product_service

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[ProductResponse])
async def list_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    sort: str = Query("created_at", regex="^(created_at|name|price)$"),
    db: AsyncSession = Depends(get_db),
):
    return await product_service.list_products(db, skip, limit, sort)

@router.post("/", response_model=ProductResponse)
async def create_product(
    data: ProductCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await product_service.create_product(db, current_user, data)

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    return await product_service.get_product(db, product_id)

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID,
    data: ProductUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await product_service.update_product(db, product_id, current_user, data)

@router.delete("/{product_id}")
async def delete_product(
    product_id: UUID,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await product_service.delete_product(db, product_id, current_user)
    return {"detail": "Product deleted"}
