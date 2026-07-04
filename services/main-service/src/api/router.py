from fastapi import APIRouter
from src.api.v1 import products

router = APIRouter(prefix="/api/main/v1")

router.include_router(products.router)