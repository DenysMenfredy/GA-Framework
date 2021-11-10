from core.problems.base import BaseIndividual
import numpy as np

class HolderTable(BaseIndividual):
    
    upper_bound = 10
    lower_bound = -10
    
    def __init__(self, dimension=None, chromosome=None):
        # self.dimension = dimension
        super().__init__(dimension, chromosome)    

    def fitnessFunction(self, ):
        return - abs(np.sin(self.chromosome[0]) * np.cos(self.chromosome[1])\
               * np.exp(abs(1- ((np.sqrt(self.chromosome[0] ** 2 \
               + self.chromosome[1] ** 2)) / np.pi))))