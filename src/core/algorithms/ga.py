from src.db.models import Problem
from .base import BaseAlgorithm

class GA(BaseAlgorithm):
    """
    Genetic Algorithm
    """
    def __init__(self, name: str, short_name: str, description: str):
        super().__init__(name, short_name, description)
        
    def run(self, problem: Problem, stop_generation: int=100, population_size: int=100, mutation_rate: float=.05, crossover_rate: float=.9, elitism: bool=True):
        """
        Run GA algorithm
        """
        population = self.initialPop(population_size, problem)
        self.evaluate(population, problem)
        self.findBest(population)
        for generation in range(stop_generation):
            population = self.reproduce(population, crossover_rate, mutation_rate, elitism)
            self.evaluate(population, problem)
            self.findBest(population)
        
        return population
