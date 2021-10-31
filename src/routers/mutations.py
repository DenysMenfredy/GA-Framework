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


@router.get("/mutations", response_model=List[schemas.MutationGet])
def read_mutations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_mutations(db, skip=skip, limit=limit)

@router.post("/mutations", response_model=schemas.Mutation)
def create_mutation(mutation: schemas.Mutation, db: Session = Depends(get_db)):
    return crud.create_mutation(db, mutation=mutation)

