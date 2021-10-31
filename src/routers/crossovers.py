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


@router.get("/crossovers", response_model=List[schemas.CrossoverGet])
def read_crossovers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_crossovers(db, skip=skip, limit=limit)

@router.post("/crossovers", response_model=schemas.Crossover)
def create_crossover(crossover: schemas.Crossover, db: Session = Depends(get_db)):
    return crud.create_crossover(db=db, crossover=crossover)
