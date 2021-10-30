from typing import List, Optional
from uuid import uuid4
from pydantic.types import UUID4

from pydantic import BaseModel


class UserBase(BaseModel):
    user_id: UUID4 = uuid4()
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    company: Optional[str]


class User(UserBase):
    class Config:
        orm_mode = True

class ProblemBase(BaseModel):
    problem_id: UUID4 = uuid4()
    problem_name: str
    description: str

    class Config:
        orm_mode = True

class AlgorithmBase(BaseModel):
    algorithm_id: Optional[UUID4]
    algorithm_name: str
    short_name: str
    description: str

    class Config:
        orm_mode = True

class ParameterBase(BaseModel):
    parameter_id: Optional[UUID4]
    parameter_name: str
    description: str

    class Config:
        orm_mode = True
