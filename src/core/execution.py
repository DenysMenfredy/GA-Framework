from datetime import datetime
from src.db.models import Problem
from src.core.algorithms.base import BaseAlgorithm
from src.core.user import User
from uuid import uuid4
from random import seed

class Execution:
    def __init__(self, id: uuid4, id_algorithm: uuid4, id_problem: uuid4, id_user: uuid4, seed: int, status:uuid4, created_at, finished_at):
        self.id = id
        self.id_algorithm = id_algorithm
        self.id_problem = id_problem
        self.id_user = id_user
        self.seed = seed
        self.status = status
        self.created_at = created_at
        self.finished_at = finished_at
    
    def getProblem(self, id_problem: uuid4) -> Problem:
        pass

    def getAlgorithm(self, id_algorithm) -> BaseAlgorithm:
        pass

    def getUser(self, id_user:uuid4) -> User:
        pass

    def save(self):
        pass
        
    def start(self):
        seed(self.seed)
        problem = self.getProblem(self.id_problem)
        algorithm = self.getAlgorithm(self.id_algorithm)
        user = self.getUser(self.id_user)
        algorithm.run(problem)
        self.status = "FINISHED" # TODO: Status predefinidos pelo banco
        self.finished_at = datetime.now()
        self.save()
        