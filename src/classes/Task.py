from abs import ABC

class Task(ABC):
    '''
    :field state: represents state of task, 0 means uncompleted, 1 means completed
    :field required_tasks: list of required subtasks to complete main task
    '''

    @abstractmethod
    def __init__(self, state=0):
        self.state = state
        self.required_tasks = list()
    
    @abstractmethod
    def complete(self):
        pass
