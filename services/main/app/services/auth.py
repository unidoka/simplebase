from sqlalchemy.ext.asyncio import AsyncSession
from ..models.user import User
from ..schemas.auth import EmailRegisterRequest, EmailLoginRequest, SmsLoginRequest

async def register_email(db: AsyncSession, data: EmailRegisterRequest):
    # TODO: реализовать
    pass

async def login_email(db: AsyncSession, data: EmailLoginRequest):
    # TODO: реализовать
    pass

async def send_sms(phone: str, code: str):
    # TODO: реализовать HTTP-запрос к провайдеру
    pass

async def store_sms_code(phone: str, code: str):
    # TODO: сохранить в Valkey с TTL 5 мин
    pass

async def verify_sms_code(phone: str, code: str) -> bool:
    # TODO: проверить код в Valkey
    return False

async def login_or_create_user_sms(db: AsyncSession, phone: str):
    # TODO: найти или создать пользователя
    pass
