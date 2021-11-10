from uuid import uuid4


class Selection:
    """
    A Selection method is used to select individuals in a population 
    """
    def ___init__(self, id:uuid4, name:str, description:str) -> None:
        """
        
        :param id: ID of the selection method
        :param name: name of the selection method
        :param description: description of the selection method
        """

        self.id = id
        self.name = name
        self.description = description


    def select(self, population):
        raise NotImplementedError