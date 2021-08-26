
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