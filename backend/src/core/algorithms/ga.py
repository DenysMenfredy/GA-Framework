from core.problems.function import Function # TODO: use problems.maximization instead of functions.mazimization
from .base import BaseAlgorithm

class GA(BaseAlgorithm):
    """
    Genetic Algorithm
    """
    def __init__(self):
        super().__init__('Genetic Algorithm', 'GA', 'Algoritmo genético pa pa pa...')
        
    def run(self, problem: Function, stop_generation: int=100, population_size: int=100, mutation_rate: float=.05, crossover_rate: float=.9, elitism: bool=True):
        """
        Run GA algorithm
        """
        self.stop_generation = stop_generation
        self.size_pop = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elitism = elitism
        self.best_individual = None
        self.crossover_method = 'two_point'

        population = self.initialPop(population_size, problem)
        self.evaluate(population, problem)
        self.findBest(population, problem.maximization)
        for _ in range(stop_generation):
            population = self.reproduce(population, problem)
            self.evaluate(population, problem)
            self.findBest(population, problem.maximization)
        
        return self.best_individual
