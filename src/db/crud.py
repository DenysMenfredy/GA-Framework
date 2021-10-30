from uuid import uuid4
from sqlalchemy.orm import Session
from pydantic.types import UUID4
from . import models, schemas


def get_user_by_id(db: Session, user_id: UUID4):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserBase):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, first_name=user.first_name, \
                          last_name=user.last_name, email=user.email, 
                          password=fake_hashed_password, company=user.company)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_problem(db: Session, problem: schemas.ProblemBase):
    # problem_id = UUID()
    # print(problem_id)
    db_problem = models.Problem(problem_name=problem.problem_name, \
                                description=problem.description)
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

def get_problems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Problem).offset(skip).limit(limit).all()


def create_algorithm(db: Session, algorithm: schemas.AlgorithmBase):
    db_algorithm = models.Algorithm(algorithm_id = algorithm.algorithm_id, \
                                    algorithm_name=algorithm.algorithm_name, \
                                    short_name=algorithm.short_name, \
                                    description=algorithm.description)

    db.add(db_algorithm)
    db.commit()
    db.refresh(db_algorithm)
    return db_algorithm

def get_algorithms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Algorithm).offset(skip).limit(limit).all()

def get_algorithm(db: Session, algorithm_id: UUID4):
    return db.query(models.Algorithm).filter(models.Algorithm.algorithm_id == algorithm_id).first()
    
def create_parameter(db: Session, parameter: schemas.ParameterBase):
    db_parameter = models.Parameter(parameter_name=parameter.parameter_name, \
                                    description=parameter.description)
    db.add(db_parameter)
    db.commit()
    db.refresh(db_parameter)
    return db_parameter

def get_parameters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parameter).offset(skip).limit(limit).all()
