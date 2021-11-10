from fastapi import APIRouter, Depends
from pydantic.types import UUID4
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

@router.get("/parameters/{parameter_id}", response_model=schemas.ParameterBase, tags=["parameters"])
def read_parameter(parameter_id: UUID4, db: Session = Depends(get_db)):
    return crud.get_parameter(db, parameter_id)

@router.post("/parameters", response_model=schemas.ParameterBase, tags=["parameters"])
def create_parameter(parameter: schemas.ParameterBase, db: Session = Depends(get_db)):
    return crud.create_parameter(db=db, parameter=parameter)