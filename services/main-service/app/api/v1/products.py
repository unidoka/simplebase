import math
from fastapi import APIRouter, Path, HTTPException
from app.models.product import Product
from app.models.user import User
from fastapi.params import Depends, Query
from app.shared.auth import get_current_user
from app.schemas.product.requests import CreateProduct
from sqlalchemy.orm import Session
from database.database import get_db
from app.schemas.product.responses import ProductResponse
from uuid import UUID
from typing import Annotated

from app.schemas.product.requests import UpdateProduct
from app.schemas.product.responses import ProductListResponse

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=ProductListResponse)
async def get_products(
    page: int = Query(1, ge=1),
    sort: str = Query("desc", pattern="^(asc|desc)$"),
    db: Session = Depends(get_db),
):
    PER_PAGE = 20

    query = db.query(Product)

    total = query.count()

    if sort == "asc":
        query = query.order_by(Product.created_at.asc())
    else:
        query = query.order_by(Product.created_at.desc())

    products = (
        query
        .offset((page - 1) * PER_PAGE)
        .limit(PER_PAGE)
        .all()
    )

    return {
        "items": [
            ProductResponse.model_validate(product)
            for product in products
        ],
        "paginate": {
            "page": page,
            "per_page": PER_PAGE,
            "total": total,
            "last_page": math.ceil(total / PER_PAGE),
        }
    }

@router.get("/{id}", response_model=ProductResponse)
async def get_product(
    id: Annotated[UUID, Path(title="uuid продукта")],
    db: Session = Depends(get_db),
):
    db_product = db.query(Product).filter(Product.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Продукт не найден")

    return ProductResponse.model_validate(db_product)


@router.post("/")
async def create(
    product: CreateProduct,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ProductResponse:
    data = product.model_dump()
    data["created_by"] = current_user.id

    new_product = Product(**data)

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return ProductResponse.model_validate(new_product)

@router.patch("/{id}")
async def update(
    product: UpdateProduct,
    id: Annotated[UUID, Path(title="uuid продукта")],
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ProductResponse:

    db_product = db.query(Product).filter(Product.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Продукт не найден")

    if current_user.id != db_product.created_by:
        raise HTTPException(status_code=401, detail="Доступ к данному ресурсу запрещен")

    data = product.model_dump(exclude_unset=True)

    for key, value in data.items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return ProductResponse.model_validate(db_product)


@router.delete("/{id}")
async def delete(
    id: Annotated[UUID, Path(title="uuid продукта")],
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    db_product = db.query(Product).filter(Product.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="Продукт не найден")

    if current_user.id != db_product.created_by:
        raise HTTPException(status_code=401, detail="Доступ к данному ресурсу запрещен")

    db.delete(db_product)
    db.commit()

    return {
        "detail": "Продукт успешно удалён"
    }