from fastapi import APIRouter, Depends
from pydantic.types import UUID4
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


@router.get("/executions", response_model=List[schemas.Execution])
def read_executions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_executions(db, skip=skip, limit=limit)

@router.get("/executions/{execution_id}", response_model=schemas.Execution)
def read_execution(execution_id: UUID4, db: Session = Depends(get_db)):
    return crud.get_execution(db, execution_id=execution_id)

@router.post("/executions", response_model=schemas.Execution)
def create_execution(execution: schemas.Execution, db: Session = Depends(get_db)):
    return crud.create_execution(db=db, execution=execution)