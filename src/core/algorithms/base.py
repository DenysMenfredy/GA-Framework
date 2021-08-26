
from random import randrange, sample, random
from src.core.problems.problem import Problem


class BaseAlgorithm:
    """
    Base class for all algorithms.
    """

    def __init__(self, name:str, short_name:str, description:str):
        """
        Initialize the algorithm.

        :param name: Name of the algorithm.
        :param short_name: Short name of the algorithm.
        :param description: Description of the algorithm.
        """
        self.name = name
        self.short_name = short_name
        self.description = description
    
    def run(self, problem: Problem, **kwargs):
        """
        Run algorithm
        """
        raise NotImplementedError

    
    def initialPop(self, size:int, problem:Problem):
        """Generate a initial population"""

        return [problem.getRandomSolution() for _ in range(size)]
    
    
    def evaluate(self, population, problem:Problem):
        """Evaluate each individual computing their fitness"""
        
        for individual in population:
            individual.fitness = problem.evaluateSolution(individual.chromosome)
    
    def reproduce(self, population, crossover_rate, mutation_rate, elitism):
        """Reproduce the population using th genetic operators"""
        
        mating_pool = self.select(population)
        new_pop = self.crossover(mating_pool)
        self.mutate(new_pop)
        new_pop.sort(key = lambda indv: indv.fitness)
        percentual = int(self.size_pop * self.crossover_rate)
        percentual = percentual if percentual % 2 == 0 else percentual + 1
        population.sort(key = lambda indv: indv.fitness, reverse=True)
                
        return new_pop + population[percentual: ]


    def crossover(self, mating_pool):
        """Mating individuals to generate offspring based in crossover rate"""
        
        new_pop = []
        percentual = int(self.size_pop * self.crossover_rate)
        percentual = percentual if percentual % 2 == 0 else percentual + 1
        size = len(mating_pool)
        
        for _ in range(0, percentual, 2):
            indv1 = mating_pool[randrange(size)]
            indv2 = mating_pool[randrange(size)]
            indv12, indv21 = self.twoPointCrossover(indv1.chromosome, indv2.chromosome) \
                             if self.crossover_method == "twoPoint"\
                             else self.onePointCrossover(indv1.chromosome, indv2.chromosome)

            new_pop.append(self.problem(dimension=self.dimension, chromosome=indv12))
            new_pop.append(self.problem(dimension=self.dimension, chromosome=indv21))
            
        return new_pop


    def onePointCrossover(self, chrm1, chrm2):
        """One point crossover method"""
        
        cut_point1 = randrange(len(chrm1))
        cut_point2 = cut_point1
        
        chrm12 = chrm1[ :cut_point1] + chrm2[cut_point1 :cut_point2] + chrm1[cut_point2: ]
        chrm21 = chrm2[ :cut_point1] + chrm1[cut_point1 :cut_point2] + chrm2[cut_point2: ]
        
        return(chrm12, chrm21)
    
    def twoPointCrossover(self, chrm1, chrm2):
        """Two point crossover method"""
        cut_point1 = randrange(len(chrm1))
        cut_point2 = cut_point1
        
        chrm12 = chrm1[ :cut_point1] + chrm2[cut_point1 :cut_point2] + chrm1[cut_point2: ]
        chrm21 = chrm2[ :cut_point1] + chrm1[cut_point1 :cut_point2] + chrm1[cut_point2: ]
        
        return(chrm12, chrm21)

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

    def findBest(self, population):
        """Get the best individual of the population based on its fitness"""
        
        best = sorted(population, key = lambda indv: indv.fitness)[0]
         
        if not self.best_individual:
            self.best_individual = best.copy()
            
        if best.fitness < self.best_individual.fitness:
            self.best_individual = best.copy()

    def plotGraphics(self):
        pass