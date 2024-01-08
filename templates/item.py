from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import List, Optional

class Users(BaseModel):
    surname: str = Field(title="Surname", max_length=30)
    name: str = Field(title="Name", max_length=30)
    patronymic: str = Field(default=None, title="Patronymic", max_length=30)
    email: str = Field(title="Email", max_length=50, min_length=5)
    password: str = Field(title="Password", min_length=8)

class UsersOut(BaseModel):
    id: int
    surname: str = Field(title="Surname", max_length=30)
    name: str = Field(title="Name", max_length=30)
    patronymic: str = Field(default=None, title="Patronymic", max_length=30)
    email: str = Field(title="Email", max_length=50, min_length=5)

    class Config:
        from_attributes = True

class Products(BaseModel):
    name: str = Field(title="Name", max_length=100)
    description: str = Field(title="Description", max_length=1000)
    price: float = Field(title="Price", gt=0)

class ProductsOut(BaseModel):
    id: int
    name: str = Field(title="Name", max_length=100)
    description: str = Field(title="Description", max_length=1000)
    price: float = Field(title="Price", gt=0)

class Orders(BaseModel):
    id_user: int
    id_products: int
    status: str = Field(title="Status", max_length=100) 

class OrdersOut(BaseModel):
    id: int
    id_user: int
    id_products: int
    status: str
    date: datetime
    items: List[UsersOut] = []

    class Config:
        from_attributes = True

    # @validator("date_order", pre=True)
    # def string_to_date(cls, v):
    #     return datetime.strptime(v, "%d-%b-%Y %H:%M:%S").date()
