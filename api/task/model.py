class Task:
    def __init__(self, task_id, name, account_id):
        self.task_id = task_id
        self.name = name
        self.account_id = account_id

    def to_json(self):
        task = {
            'task_id': self.task_id,
            'name': self.name,
            'account_id': self.account_id
        }
        return task