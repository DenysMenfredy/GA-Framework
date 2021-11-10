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


@router.get("/functions", response_model=List[schemas.FunctionGet])
def get_functions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_functions(db, skip=skip, limit=limit)

@router.post("/functions", response_model=schemas.FunctionCreate)
def create_function(function: schemas.FunctionCreate, db: Session = Depends(get_db)):
    return crud.create_function(db=db, function=function)