from uuid import uuid4

class Operator:
    '''
        Operator class
    '''
    def __init__(self, id: uuid4, name:str, description:str, type:str):
        '''
        :params id: Id of the operator
        :params name: Name of the operator
        :params description: Descriptions of the operator
        :params type: Type of the operator
        '''
        self.id = id
        self.name = name
        self.description = description
        self.type = type