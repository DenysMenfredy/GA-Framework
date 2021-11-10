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


@router.get("/selections", response_model=List[schemas.Selection])
def read_selections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_selections(db, skip=skip, limit=limit)

@router.post("/selections", response_model=schemas.Selection)
def create_selection(selection: schemas.Selection, db: Session = Depends(get_db)):
    return crud.create_selection(db=db, selection=selection)
    