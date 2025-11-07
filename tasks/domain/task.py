from datetime import date
# business rules, tells us what is allowed and what is not allowed in our application
# heart of the project.
class Task:
    #when creating a task here are the rules to follow 
    def __init__(self, id=None, title="", is_done=False, due_date=None, priority="normal"):
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        if priority not in ["low", "normal", "high"]:
            raise ValueError("Priority must be 'low', 'normal', or 'high'.")

        if due_date and due_date < date.today():
            raise ValueError("Due date cannot be in the past.")
        self.id = id
        self.title = title
        self.is_done = is_done
        self.due_date = due_date
        self.priority = priority
# when updating a task here are the rules to follow
    def is_overdue(self):
        #Return True if task is overdue
        return not self.is_done and self.due_date and self.due_date < date.today()

    def update_due_date(self, new_due_date):
        if new_due_date and new_due_date < date.today():
            raise ValueError("Due date cannot be in the past.")
        self.due_date = new_due_date

    def change_priority(self, new_priority):
        if new_priority not in ["low", "normal", "high"]:
            raise ValueError("Invalid priority level.")
        self.priority = new_priority

    def mark_done(self):
        if self.is_done:
            raise Exception("Task already completed.")
        self.is_done = True
