import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Enum,
    Text,
    ForeignKey,
    Numeric,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, default="NONE")
    password = Column(String, default="NONE")
    name = Column(String, default="NONE")
    contact = Column(String, default="NONE")
    address = Column(String, default="NONE")
    role = Column(Enum("admin", "super_admin", name="user_roles"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_deleted = Column(BIT(1), default=0)
