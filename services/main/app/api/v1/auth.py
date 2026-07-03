from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...core.database import get_db
from ...core.security import get_current_user
from ...schemas.auth import (
    EmailRegisterRequest, SmsRegisterRequest,
    EmailLoginRequest, SmsLoginRequest,
    TokenResponse, UserResponse
)
from ...models.user import User
from ...services import auth as auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register/email", response_model=TokenResponse)
async def register_email(
    data: EmailRegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    return await auth_service.register_email(db, data)

@router.post("/login/email", response_model=TokenResponse)
async def login_email(
    data: EmailLoginRequest,
    db: AsyncSession = Depends(get_db),
):
    return await auth_service.login_email(db, data)

@router.post("/send-sms")
async def send_sms(
    phone: SmsRegisterRequest,
):
    # генерация кода, сохранение, отправка
    pass

@router.post("/login/sms", response_model=TokenResponse)
async def login_sms(
    data: SmsLoginRequest,
    db: AsyncSession = Depends(get_db),
):
    return await auth_service.login_or_create_user_sms(db, data.phone)

@router.get("/me", response_model=UserResponse)
async def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user
