from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: Optional[constr(min_length=3, max_length=25)] = None
    password: Optional[constr(min_length=6)] = None
    name: str
    contact: str
    address: str
    role: Optional[Literal["admin", "super_admin", "customer", "rider"]] = None
    is_deleted: Optional[bool] = 0
