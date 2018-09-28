class Task:
    def __init__(self, task_id, task_name, account_id):
        self.task_id = task_id
        self.task_name = task_name
        self.account_id = account_id

    def to_json(self):
        task = {
            'task_id': self.task_id,
            'name': self.task_name,
            'account_id': self.account_id
        }
        return task


tasks = []
deleted_tasks = []
