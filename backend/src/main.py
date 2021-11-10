from typing import List
from uuid import uuid4

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import crud, models, schemas
from db.database import SessionLocal, engine

import core.algorithms as algorithms
from core.algorithms.ga import GA
from core.problems.function import Sphere

from routers.users import router as users_router
from routers.problems import router as problems_router
from routers.algorithms import router as algorithms_router
from routers.parameters import router as parameters_router
from routers.status import router as status_router
from routers.selections import router as selections_router
from routers.operators import router as operators_router
from routers.mutations import router as mutations_router
from routers.crossovers import router as crossovers_router
from routers.functions import router as functions_router
from routers.executions import router as executions_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)
app.include_router(problems_router)
app.include_router(algorithms_router)
app.include_router(parameters_router)
app.include_router(status_router)
app.include_router(selections_router)
app.include_router(operators_router)
app.include_router(mutations_router)
app.include_router(crossovers_router)
app.include_router(functions_router)
app.include_router(executions_router)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def hello_world():
    return {"message": "Hello World"}




