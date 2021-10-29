from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel
from pydantic.types import UUID4


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
    user_id: UUID4
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    company: Optional[str]


class UserCreate(UserBase):
    # email: str
    password: str


class User(UserBase):
    user_id: int
    # is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class ProblemBase(BaseModel):
    problem_id: Optional[UUID4]
    problem_name: str
    description: str

class AlgorithmBase(BaseModel):
    algorithm_id: Optional[UUID4]
    algorithm_name: str
    short_name: str
    description: str