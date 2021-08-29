from typing import List
from uuid import uuid4

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

import core.algorithms as algorithms
from core.algorithms.ga import GA
from core.problems.function import Sphere

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/exec")
def execute_algorithm(params: dict):
    print(params)
    problem = Sphere()
    ag = GA()
    best_solution = ag.run(problem)

    return {"best fitness": best_solution.fitness}

@app.post("/problem")
def create_problem(problem: schemas.ProblemBase, db: Session = Depends(get_db)):
    problem.id = uuid4()
    return crud.create_problem(db, problem)

@app.post("/algorithm")
def create_algorithm(algorithm: schemas.AlgorithmBase, db: Session = Depends(get_db)):
    algorithm.id = uuid4()
    return crud.create_algorithm(db, algorithm)

@app.get("/algorithms")
def get_algorithms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_algorithms(db, skip=skip, limit=limit)

@app.get("/problems")

@app.post("/execution")

@app.get("/problems/")
def get_problems(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    problems = crud.get_problems(db, skip=skip, limit=limit)
    return problems


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # print(user)
    db_user = crud.get_user_by_email(db, email=user.notification_email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items