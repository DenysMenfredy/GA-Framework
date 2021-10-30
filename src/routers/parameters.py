from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from db import crud, schemas
from db.database import SessionLocal

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/parameters", response_model=List[schemas.ParameterBase], tags=["parameters"])
def read_parameters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_parameters(db, skip=skip, limit=limit)
    
@router.post("/parameters", response_model=schemas.ParameterBase, tags=["parameters"])
def create_parameter(parameter: schemas.ParameterBase, db: Session = Depends(get_db)):
    return crud.create_parameter(db=db, parameter=parameter)