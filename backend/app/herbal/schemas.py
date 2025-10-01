from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, constr


class UserBase(BaseModel):
    username: Optional[constr(min_length=3, max_length=25)] = None
    password: Optional[constr(min_length=6)] = None
    role: Optional[Literal["admin", "super_admin"]] = None
    is_deleted: Optional[bool] = 0


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class HerbalPlantBase(BaseModel):
    name: str
    scientific_name: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    is_deleted: Optional[bool] = 0


class HerbalPlantCreate(HerbalPlantBase):
    pass


class HerbalPlant(HerbalPlantBase):
    id: int

    class Config:
        from_attributes = True


class BarangayBase(BaseModel):
    name: str
    municipality: str
    captain_official: Optional[str] = None
    is_deleted: Optional[bool] = 0


class BarangayCreate(BarangayBase):
    pass


class Barangay(BarangayBase):
    id: int

    class Config:
        from_attributes = True
