from fastapi import APIRouter, Depends
from db import crud, schemas
from db.database import SessionLocal
from pydantic.types import UUID4

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/algorithms", tags=["algorithms"])
def get_algorithms(skip: int = 0, limit: int = 100, db: SessionLocal = Depends(get_db)):
    return crud.get_algorithms(db, skip=skip, limit=limit)


@router.get("/algorithms/{id}", tags=["algorithms"])
def get_algorithm(algorithm_id: UUID4, db: SessionLocal = Depends(get_db)):
    return crud.get_algorithm(db, algorithm_id=algorithm_id)


@router.post("/algorithms", tags=["algorithms"])
def create_algorithm(algorithm: schemas.AlgorithmBase, db: SessionLocal = Depends(get_db)):
    return crud.create_algorithm(db=db, algorithm=algorithm)