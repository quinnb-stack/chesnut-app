import datetime

from sqlalchemy import Column, DateTime, Integer, String, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import BIT

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, default="NONE")
    password = Column(String, default="NONE")
    role = Column(Enum("admin", "super_admin", name="user_roles"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_deleted = Column(BIT(1), default=0)


class HerbalPlant(Base):
    __tablename__ = "herbal_plants"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    scientific_name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String(255), nullable=True)
    is_deleted = Column(BIT(1), nullable=False, default=0)


class Barangay(Base):
    __tablename__ = "barangays"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    municipality = Column(String(150), nullable=False)
    captain_official = Column(String(150), nullable=True)
    is_deleted = Column(BIT(1), nullable=False, default=0)
