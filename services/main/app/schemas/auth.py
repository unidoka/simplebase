from pydantic import BaseModel, EmailStr, Field, validator
from uuid import UUID
from datetime import datetime

class EmailRegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

class SmsRegisterRequest(BaseModel):
    phone: str = Field(..., regex=r"^\+?[1-9]\d{1,14}$")

class EmailLoginRequest(BaseModel):
    email: EmailStr
    password: str

class SmsLoginRequest(BaseModel):
    phone: str = Field(..., regex=r"^\+?[1-9]\d{1,14}$")
    code: str = Field(..., regex=r"^\d{6}$")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: UUID
    email: str | None
    phone: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime | None
