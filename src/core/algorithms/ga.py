import numpy as np
import matplotlib.pyplot as plt
from random import sample, randrange, random


class GeneticAlgorithm():
    def __init__(self, **params):
        self.size_pop = params["size_pop"]
        self.num_generations = params["generations"]
        self.crossover_rate = params["crossover_rate"]
        self.mutation_rate = params["mutation_rate"]
        self.best_individual = None
        self.agent = params["agent"]
        self.agent_dimension = params["agent_dimension"]

    def start(self):
        
        self.resetData()
        population =  self.initialPop()
        self.evalute(population)
        self.findBest(population)
        self.saveData(population)
        for _ in range(self.num_generations):
              population = self.reproduce(population)
              self.evalute(population)
              self.findBest(population)
              self.saveData(population)

    
    
    def initialPop(self, ):
        """Generate a initial population"""

        return [self.agent(dimension=self.agent_dimension) for _ in range(self.size_pop)]
    
    
    def evalute(self, population):
        """Evaluate each individual computing their fitness"""
        
        for individual in population:
            individual.fitness = individual.fitnessFunction()
    
    def reproduce(self, population):
        """Reproduce the population using th genetic operators"""
        
        mating_pool = self.select(population)
        new_pop = self.crossover(mating_pool)
        self.mutate(new_pop)
        new_pop.sort(key = lambda indv: indv.fitness)
        percentual = int(self.size_pop * self.crossover_rate)
        percentual = percentual if percentual % 2 == 0 else percentual + 1
        population.sort(key = lambda indv: indv.fitness, reverse=True)
                
        return new_pop + population[percentual: ]

    def evalute(self, population):
        pass
    
    def crossover(self, mating_pool):
        """Mating individuals to generate offspring based in crossover rate"""
        
        new_pop = []
        percentual = int(self.size_pop * self.crossover_rate)
        percentual = percentual if percentual % 2 == 0 else percentual + 1
        size = len(mating_pool)
        
        for _ in range(0, percentual, 2):
            indv1 = mating_pool[randrange(size)]
            indv2 = mating_pool[randrange(size)]
            indv12, indv21 = self.twoPointCrossover(indv1.chromosome, indv2.chromosome)
            new_pop.append(self.agent(dimension=self.agent_dimension, chromosome=indv12))
            new_pop.append(self.agent(dimension=self.agent_dimension, chromosome=indv21))
            
        return new_pop

    def mutate(self, population):
        """Mutate the individuals based in mutation rate"""
        
        for indiv in population:
            mutate = random() < self.mutation_rate
            if mutate:
                size = len(indiv.chromosome)
                n1, n2 = randrange(size), randrange(size)
                indiv.chromosome = indiv.chromosome[:n1] + [indiv.chromosome[n2]] + \
                indiv.chromosome[n1+1:n2] + [indiv.chromosome[n1]] + indiv.chromosome[n2+1: ]

    def select(self, population):
        """Select parents to mating using tournament selection method"""
        
        mating_pool = []
        amount = 3
        percentual = int(self.size_pop * self.crossover_rate)
        percentual = percentual if percentual % 2 == 0 else percentual + 1
        
        for _ in range(percentual):
            selecteds = sample(population, amount)
            best = sorted(selecteds ,key = lambda indv: indv.fitness)[0]
            mating_pool.append(best)
            
        return mating_pool

    def bestIndividual(self, population):
        """Get the best individual of the population based on its fitness"""
        
        best = sorted(population, key = lambda indv: indv.fitness)[0]
         
        if not self.best_individual:
            self.best_individual = best.copy()
            
        if best.fitness < self.best_individual.fitness:
            self.best_individual = best.copy()

    def plotGraphics(self):
        pass


