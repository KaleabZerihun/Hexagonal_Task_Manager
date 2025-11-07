from abc import ABC, abstractmethod

class TaskRepositoryPort(ABC):
    #the port defines what functions the adapter can implement

    @abstractmethod
    def list_tasks(self):
        pass

    @abstractmethod
    def add_task(self, task):
        pass

    @abstractmethod
    def get_task(self, task_id):
        pass

    @abstractmethod
    def update_task(self, task):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass
