

class Individual:
    """
    An individual in the population.
    """
    def __init__(self, chromosome, fitness = None):
        self.fitness = fitness
        self.chromosome = chromosome

    def copy(self):
        return Individual(self.chromosome, self.fitness)