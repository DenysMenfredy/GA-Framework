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


@router.get("/status", response_model=List[schemas.Status])
def get_status(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_status(db, skip=skip, limit=limit)

@router.post("/status", response_model=schemas.Status)
def create_status(status: schemas.Status, db: Session = Depends(get_db)):
    return crud.create_status(db=db, status=status)
