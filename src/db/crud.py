from uuid import uuid4
from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.notification_email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(login=user.login, name=user.name, notification_email=user.notification_email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_problem(db: Session, problem: schemas.ProblemBase):
    # problem_id = uuid4()
    # print(problem_id)
    db_problem = models.Problem(name=problem.name, description=problem.description)
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

def get_problems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Problem).offset(skip).limit(limit).all()


def create_algorithm(db: Session, algorithm: schemas.AlgorithmBase):
    db_algorithm = models.Algorithm(algorithm_id = algorithm.algorithm_id, algorithm_name=algorithm.algorithm_name, short_name=algorithm.short_name, description=algorithm.description)
    db.add(db_algorithm)
    db.commit()
    db.refresh(db_algorithm)
    return db_algorithm

def get_algorithms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Algorithm).offset(skip).limit(limit).all()
    
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item