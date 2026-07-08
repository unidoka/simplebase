import uuid

from sqlalchemy import Column, UUID, String, ForeignKey, Boolean, DateTime, DECIMAL
from sqlalchemy.orm import relationship, foreign
from database.database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID, primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    description = Column(String, index=False)
    price = Column(DECIMAL, index=True)

    created_by = Column(UUID, ForeignKey("users.id"))

    creator = relationship("User")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)