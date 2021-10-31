from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import crud, schemas
from db.database import SessionLocal
from typing import List


router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/operators", response_model=List[schemas.Operator])
def read_operators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_operators(db, skip=skip, limit=limit)

@router.post("/operators", response_model=schemas.Operator)
def create_operator(operator: schemas.Operator, db: Session = Depends(get_db)):
    return crud.create_operator(db=db, operator=operator)