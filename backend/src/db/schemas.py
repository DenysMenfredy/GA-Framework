from typing import Optional
from pydantic.types import UUID4 

from pydantic import BaseModel
from datetime import datetime



class UserBase(BaseModel):
    user_id: Optional[UUID4]
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
    problem_id: Optional[UUID4]
    problem_name: str
    description: str

    class Config:
        orm_mode = True

class Function(BaseModel):
    function_id: Optional[UUID4]
    minimum_dimension: int
    maximum_dimension: int
    upper_bound: float
    lower_bound: float
    optimum: float
    maximization: bool

class FunctionCreate(Function):
    problem_id: UUID4
    
    class Config:
        orm_mode = True

class FunctionGet(Function):
    problem_id: UUID4
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


class Execution(BaseModel):
    execution_id: Optional[UUID4]
    problem_id: UUID4
    algorithm_id: UUID4
    user_id: UUID4
    status_id: UUID4
    selection_id: UUID4
    crossover_id: UUID4
    mutation_id: UUID4
    execution_time: Optional[float]
    seed: float
    created_at: Optional[datetime]
    finished_at: Optional[datetime]

    class Config:
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True