import uuid
from datetime import datetime

from sqlalchemy import Column, UUID, String, Boolean, DateTime

from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    password = Column(String)
    blocked = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
