import numpy as np
from base import BaseIndividual

class Rastrigin(BaseIndividual):
    def __init__(self, dimension, chromosome):
        super().__init__(dimension=dimension, chromosome=chromosome)
        self.upper_bound = 5.12
        self.lower_bound = -5.12

    def fitnessFunction(self):
        return (10 * self.dimension) + sum([(x_i ** 2) - 10 * \
                np.cos((2 * np.pi) * x_i) for x_i in self.chromosome])


if __name__ == '__main__':
    t = Rastrigin(dimension=10, chromosome=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    print(t.fitnessFunction())