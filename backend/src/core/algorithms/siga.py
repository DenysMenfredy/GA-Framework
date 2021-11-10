from .ga import GA

class SIGA(GA):
    """
    Genetic Algorithm
    """
    def __init__(self, name: str, short_name: str, description: str):
        super().__init__(name, short_name, description)
        