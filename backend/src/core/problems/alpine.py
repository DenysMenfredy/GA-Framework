from base import BaseIndividual
import numpy as np

class Alpine(BaseIndividual):
    def __init__(self, dimension, chromosome):
        super().__init__(dimension=dimension, chromosome=chromosome)
        self.upper_bound = 10
        self.lower_bound = -10

    def fitnessFunction(self):
        
        return abs(sum([(sum([x_i * np.sin(x_i) + 0.1 * x_i for x_i in self.chromosome])) \
            for _ in range(self.dimension - 1)]))
                
        


if __name__ == '__main__':
    t = Alpine(dimension=10, chromosome=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    print(t.fitnessFunction())