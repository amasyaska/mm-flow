from abs import ABC

class Task(ABC):

    @abstractmethod
    def __init__(self, state='completed'):
        self.state = state
    
    @abstractmethod
    def complete(self):
        pass
