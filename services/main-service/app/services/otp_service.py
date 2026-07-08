# app/services/otp_service.py
import random
import json
from datetime import datetime, timedelta
from database.cache import cache_client

OTP_TTL_SECONDS = 300

def generate_otp() -> str:
    return str(random.randint(100000, 999999))


def save_otp(identifier: str, code: str, otp_type: str = "login") -> bool:
    """
    Сохраняет OTP в Valkey с TTL 5 минут.
    identifier: телефон или email
    """
    key = f"otp:{identifier}"
    data = {
        "code": code,
        "type": otp_type,
        "created_at": datetime.utcnow().isoformat()
    }

    try:
        cache_client.setex(key, OTP_TTL_SECONDS, json.dumps(data))
        return True
    except Exception as e:
        print(f"❌ Cache error saving OTP: {e}")
        return False


def verify_otp(identifier: str, code: str) -> bool:
    """
    Проверяет код и удаляет его при успехе (чтобы нельзя было использовать дважды).
    """
    key = f"otp:{identifier}"
    stored_data = cache_client.get(key)

    if not stored_data:
        return False

    data = json.loads(stored_data)

    if data["code"] == code:
        cache_client.delete(key)
        return True

    return False


def delete_otp(identifier: str):
    """Принудительное удаление (например, при смене номера)"""
    cache_client.delete(f"otp:{identifier}")