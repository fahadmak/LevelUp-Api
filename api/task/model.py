class Task:
    def __init__(self, task_id, task_name, account_id, marked=False):
        self.task_id = task_id
        self.task_name = task_name
        self.account_id = account_id
        self.marked = marked

    def to_json(self):
        task = {
            'task_id': self.task_id,
            'name': self.task_name,
            'account_id': self.account_id,
            'Marked': self.marked
        }
        return task

task1 = Task(1, 'fahad', 1)
task2 = Task(2, 'fahad334', 5)
task3 = Task(3, 'fahad334', 4)
tasks = [task1, task2, task3]
deleted_tasks = []
