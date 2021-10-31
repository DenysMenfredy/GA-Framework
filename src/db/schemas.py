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

class Function(BaseModel):
    function_id = UUID4
    minimum_dimension: int
    maximum_dimension: int
    upper_bound: float
    lower_bound: float
    optimum: float
    maximization: bool

    class Config:
        orm_mode = True

class FunctionCreate(Function):
    problem_id: UUID4
    
    class Config:
        orm_mode = True

class FunctionGet(Function, ProblemBase):

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

class Status(BaseModel):
    status_id: Optional[UUID4]
    status_name: str
    description: str

    class Config:
        orm_mode = True

class Selection(BaseModel):
    selection_id: Optional[UUID4]
    selection_name: str
    description: str

    class Config:
        orm_mode = True

class Operator(BaseModel):
    operator_id: Optional[UUID4]
    operator_name: str
    operator_type: str
    description: str

    class Config:
        orm_mode = True

class Crossover(BaseModel):
    crossover_id: Optional[UUID4]
    crossover_rate: float
    parameter_id: UUID4

    class Config:
        orm_mode = True

class Mutation(BaseModel):
    mutation_id: Optional[UUID4]
    mutation_rate: float
    parameter_id: UUID4

    class Config:
        orm_mode = True

class MutationGet(Mutation):
    parameter_name: str
    description: str

    class Config:
        orm_mode = True

class CrossoverGet(Crossover):
    parameter_name: str
    description: str

    class Config:
        orm_mode = True