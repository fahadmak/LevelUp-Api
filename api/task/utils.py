from api.task.model import tasks


def search_task_by_id(task_id):
    if not tasks:
        return None
    for task in tasks:
        if task_id == task.task_id:
            return task
    return None


def search_task_by_task_name(task_name):
    if not tasks:
        return None
    for task in tasks:
        if task_name == task.task_name:
            return task
    return None


def search_task_by_account_id(account_id):
    if not tasks:
        return None
    for task in tasks:
        if account_id == task.account_id:
            return task
    return None
