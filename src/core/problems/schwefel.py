import numpy as np
from base import BaseIndividual


class Schwefel(BaseIndividual):
    """Modified Schwefel CEC 2014"""
    def __init__(self, dimension, chromosome):
        super().__init__(dimension=dimension, chromosome=chromosome)
        self.upper_bound = 100
        self.lower_bound = -100


    def fitnessFunction(self):
        
        y = 0
        for x_i in self.chromosome:
            z_i = self.z_i(x_i)
            y += 418.9829 * self.dimension - sum([self.g_zi(z_i) for _ in range(self.dimension)])
        
        return y

    def z_i(self, x):
        return x + 4.209687462275036e2
        
        
    def g_zi(self, z):
        D = self.dimension
        if abs(z) <= 500:
            return z * np.sin(np.power(abs(z), 0.5))
        
        if z > 500:
            return (500 - (z % 500)) * np.sin(np.sqrt(abs(500 - (z % 500))))\
                    - (np.power((z - 500), 2) / 10000 * D)
        
        if z < -500:
            return ((abs(z) % 500) - 500) * np.sin(np.sqrt(abs((abs(z) % 500) - 500)))\
                    - (np.power((z + 500), 2) / 10000 * D)


if __name__ == '__main__':
    t = Schwefel(dimension=10, chromosome=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    print(t.fitnessFunction())