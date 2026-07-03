from fastapi import APIRouter
from .auth import router as auth_router
from .products import router as products_router

router = APIRouter(prefix="/api/v1")
router.include_router(auth_router)
router.include_router(products_router)
