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


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class CustomerBase(BaseModel):
    behavioral_score: Optional[float] = 0.0
    cancel_count: Optional[int] = 0


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class BranchBase(BaseModel):
    user_id: int
    name: str
    address: Optional[str] = None
    is_deleted: Optional[bool] = 0


class BranchCreate(BranchBase):
    pass


class Branch(BranchBase):
    id: int

    class Config:
        from_attributes = True


class RiderBase(BaseModel):
    branch_id: int
    user_id: int
    is_deleted: Optional[bool] = 0


class RiderCreate(RiderBase):
    pass


class Rider(RiderBase):
    id: int

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    name: str
    price: float
    image: Optional[str] = None
    description: Optional[str] = None
    is_deleted: Optional[bool] = 0


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True


class BranchProductBase(BaseModel):
    product_id: int
    branch_id: int
    quantity: int


class BranchProductCreate(BranchProductBase):
    pass


class BranchProduct(BranchProductBase):
    id: int
    product: Optional[Product] = None
    branch: Optional[Branch] = None

    class Config:
        from_attributes = True


class BranchWithProducts(BaseModel):
    branch_id: int
    products: List[Product]

    class Config:
        orm_mode = True
