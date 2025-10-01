from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, constr


class UserBase(BaseModel):
    username: Optional[constr(min_length=3, max_length=25)] = None
    password: Optional[constr(min_length=6)] = None
    role: Optional[Literal["admin", "super_admin"]] = None
    is_deleted: Optional[bool] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
