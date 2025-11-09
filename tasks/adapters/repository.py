from tasks.models import TaskModel
from tasks.domain.task import Task
from tasks.domain.ports import TaskRepositoryPort
#this adapter talks to the database and handles presistence
class TaskRepository(TaskRepositoryPort):
    def list_tasks(self):
        return [
            Task(
                id=t.id,
                title=t.title,
                is_done=t.is_done,
                due_date=t.due_date,
                priority=t.priority,
                validate_due_date=False,
            )
            for t in TaskModel.objects.all()
        ]

    def add_task(self, task: Task):
        TaskModel.objects.create(
            title=task.title,
            is_done=task.is_done,
            due_date=task.due_date,
            priority=task.priority,
        )

    def delete_task(self, task_id):
        TaskModel.objects.filter(id=task_id).delete()

    def get_task(self, task_id):
        t = TaskModel.objects.get(id=task_id)
        return Task(
            id=t.id,
            title=t.title,
            is_done=t.is_done,
            due_date=t.due_date,
            priority=t.priority,
            validate_due_date=False,
        )

    def update_task(self, task: Task):
        t = TaskModel.objects.get(id=task.id)
        t.title = task.title
        t.is_done = task.is_done
        t.due_date = task.due_date
        t.priority = task.priority
        t.save()
