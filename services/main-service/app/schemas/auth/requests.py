from pydantic import BaseModel, EmailStr, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber

class EmailLoginRequest(BaseModel):
    email: EmailStr

class EmailConfirmRequest(BaseModel):
    code: str

class SmsLoginRequest(BaseModel):
    phone: PhoneNumber = Field(description="Номер телефона")

class SmsConfirmRequest(BaseModel):
    code: str


class RegisterViaPhoneRequest(BaseModel):
    phone: PhoneNumber = Field(description="Номер телефона")

    password: str = Field(min_length=8, description="Минимум 8 символов")

    @field_validator('password')
    @classmethod
    def check_password_strength(cls, v):
        return v

class RegisterViaEmailRequest(BaseModel):
    email: EmailStr
    password: str