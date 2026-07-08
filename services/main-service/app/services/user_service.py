from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user.response import UserCreateResponse
from app.shared.auth import hash_password


def create_user(
    db: Session,
    **kwargs
) -> UserCreateResponse:
    phone = kwargs.get("phone")
    email = kwargs.get("email")
    password = kwargs.get("password")

    filters = []
    if phone:
        filters.append(User.phone == phone)
    if email:
        filters.append(User.email == email)

    if not filters:
        raise ValueError("Нужен хотя бы email или phone")

    db_user = db.query(User).filter(or_(*filters)).first()

    if db_user:
        errors = {}
        if phone and db_user.phone == phone:
            errors["phone"] = "Пользователь с таким телефоном уже зарегистрирован"
        if email and db_user.email == email:
            errors["email"] = "Пользователь с такой почтой уже зарегистрирован"

        return UserCreateResponse(
            created=False,
            errors=errors,
            user=None
        )

    if password:
        kwargs["password"] = hash_password(password)

    user = User(**kwargs)
    db.add(user)
    db.commit()
    db.refresh(user)

    return UserCreateResponse(
        created=True,
        errors=None,
        user=user
    )