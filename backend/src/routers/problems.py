from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import crud, schemas
from db.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/problems", tags=["problems"])
def get_problems(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    return crud.get_problems(db, skip=skip, limit=limit)

@router.post("/problems", tags=["problems"])
def create_problem(problem: schemas.ProblemBase, db: Session = Depends(get_db)):
    return crud.create_problem(db, problem)