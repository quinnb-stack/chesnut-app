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
    role = Column(
        Enum("admin", "super_admin", "customer", "rider", name="user_roles"),
        nullable=False,
    )
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_deleted = Column(BIT(1), default=0)

    customers = relationship("Customer", back_populates="user")
    branches = relationship("Branch", back_populates="user")


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    behavioral_score = Column(Numeric(5, 2), default=0.00)
    cancel_count = Column(Integer, default=0)

    user = relationship("User", back_populates="customers")


class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=True)
    is_deleted = Column(BIT(1), default=0)

    user = relationship("User", back_populates="branches")
