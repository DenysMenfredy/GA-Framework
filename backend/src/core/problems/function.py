from core.individual import Individual
import numpy as np
from .problem import Problem

class Function(Problem):
    """
    A function is a mathematical expression that can be evaluated to a number.
    """
    def __init__(self, name:str, description:str, minimum_dimension:int, maximum_dimension:int, upper_bound:float, lower_bound:float, optimum:float, maximization:bool):
        """
        Initializes a new instance of the Function class.

        :param name: The name of the function.
        :param description: The description of the function.
        :param minimum_dimension: The minimum dimension of the function.
        :param maximum_dimension: The maximum dimension of the function.
        :param upper_bound: The upper bound of the function.
        :param lower_bound: The lower bound of the function.
        :param optimum: The optimum of the function.
        :param maximization: A boolean value indicating whether the function is maximization or minimization.
        """
        super().__init__(name, description)
        self.minimum_dimension = minimum_dimension
        self.maximum_dimension = maximum_dimension
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.optimum = optimum
        self.maximization = maximization

    def evaluate(self, *args):
        """
        Evaluates the function.

        :param args: The arguments to the function.
        :return: The result of the function.
        """
        raise NotImplementedError("Function.evaluate is not implemented")
    
    def getRandomSolution(self):
        """
        Gets a random solution.

        :return: A random solution.
        """
        raise NotImplementedError("Function.getRandomSolution is not implemented")
    


class Sphere(Function):
    """
    A Sphere is a function that represents the function f(x) = x^2.
    """
    def __init__(self):
        name = "Sphere"
        description = "A Sphere is a function that represents the function f(x) = x^2."
        minimum_dimension = 3
        maximum_dimension = 256
        upper_bound = 5.12
        lower_bound = -5.12
        optimum = 0
        maximization = False
        super().__init__(name, description, minimum_dimension, maximum_dimension, upper_bound, lower_bound, optimum, maximization)
    
    def evaluate(self, chromosome:np.ndarray):
        return sum(chromosome**2)

    def getRandomSolution(self, size:int=30): # TODO: Implement dimension in model
        return Individual(np.random.uniform(self.lower_bound, self.upper_bound, size))