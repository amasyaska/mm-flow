from abc import ABC

class Resource(ABC):
    '''
    :field state: describes state of a resource, where 1 - resource is full, 0 - resource is fully exhausted
    '''

    @abstractmethod
    def __init__(self, state=1):
        self.state = state
