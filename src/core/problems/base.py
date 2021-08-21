from random import uniform


class BaseIndividual(object):
    """
    An individual in the population.
    """

    upper_bound = None
    lower_bound = None

    def __init__(self, dimension=None, chromosome=None):
        self.dimension = dimension
        self.chromosome = chromosome if chromosome else self.randomChromosome()
        self.fitness = 0

    def randomChromosome(self):
        """
        Create a random chromosome.
        """

        return [uniform(self.lower_bound, self.upper_bound) for _ in range(self.dimension)]

    def fitnessFunction(self):
        """
        Calculate the fitness of the individual.
        """

        raise NotImplementedError

    
    def copy(self):
        """
        Create a copy of the individual.
        """

        copy = Individual(self.dimension, self.chromosome)
        copy.fitness = self.fitness

        return copy

    def __str__(self):
        return f'Chromosome: {self.chromosome}\nFitness: {self.fitness}\n'

    