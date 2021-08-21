from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    login: str
    name: str
    notification_email: str


class UserCreate(UserBase):
    # email: str
    password: str


class User(UserBase):
    id: int
    # is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True