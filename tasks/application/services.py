from datetime import datetime
from tasks.domain.task import Task
# the application decides what to do when a user takes an action it's like a coordinator
class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def get_all_tasks(self):
        return self.repository.list_tasks()

    def create_task(self, title, due_date_str, priority):
        if due_date_str:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        else:
            due_date = None
        #calls the domain to create a task
        task = Task(title=title, due_date=due_date, priority=priority)
        self.repository.add_task(task)


    def delete_task(self, task_id):
        self.repository.delete_task(task_id)

    def get_task(self, task_id):
        return self.repository.get_task(task_id)

    def update_task(self, task_id, title, due_date_str, priority):
        if due_date_str:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        else:
            due_date = None
        task = self.repository.get_task(task_id)
        task.title = title
        task.update_due_date(due_date)
        task.change_priority(priority)
        self.repository.update_task(task)
