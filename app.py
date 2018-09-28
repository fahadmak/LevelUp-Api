from flask import Flask, request, jsonify

from api.auth.model import accounts, Account, logged_in_accounts
from api.task.model import tasks, Task, deleted_tasks

from api.auth.utils import search_account_by_username, search_account_by_id
from api.task.utils import search_task_by_id


app = Flask(__name__)


@app.route('/auth/signup', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')
    if not all([name, username, password]):
        return jsonify({'message': 'Please fill missing fields'})
    for item in [name, username, password]:
        if not isinstance(item, str):
            return jsonify({'message': 'Please input correct information'})
        elif not item.isalpha():
            return jsonify({'message': 'Please input correct information'})
    account_id = max([account.account_id for account in accounts]) + 1 if accounts else 1
    account = Account(account_id, name, username, password)
    accounts.append(account)
    return jsonify({'message': '{} of ID {} has created an account'.format(username, account.account_id)})


@app.route('/auth/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if not all([username, password]):
        return jsonify({'message': 'Please fill missing fields'})
    account = search_account_by_username(username)
    if not account:
        return jsonify({'message': 'This account does not exist'})
    for item in [username, password]:
        if not isinstance(item, str):
            return jsonify({'message': 'Please input correct information'})
    if account.password != password:
        return jsonify({'message': 'User name and password do not match'})
    if account in logged_in_accounts:
        return jsonify({'message': 'You are already logged in'})
    logged_in_accounts.append(account)
    return jsonify({'message': '{} you have logged in'.format(username)})


@app.route('/auth/logout', methods=['POST'])
def logout_user():
    data = request.json
    username = data.get('username')
    if not username:
        return jsonify({'message': 'Please fill missing fields'})
    if not isinstance(username, str):
        return jsonify({'message': 'Please input correct information'})
    account = search_account_by_username(username)
    if not account:
        return jsonify({'message': 'This account does not exist'})
    if account not in logged_in_accounts:
        return jsonify({'message': 'You must be logged in to logged out'})
    logged_out_username = account.username
    logged_in_accounts.remove(account)
    return jsonify({'message': '{} you have logged out, until next time '.format(logged_out_username)})


@app.route('/auth/delete/<int:account_id>', methods=['DELETE'])
def delete_user(account_id):
    account = search_account_by_id(account_id)
    if not account:
        return jsonify({'message': 'This account does not exist'})
    if account not in logged_in_accounts:
        return jsonify({'message': 'You must be logged in to deleted your account'})
    account_name = account.username
    logged_in_accounts.remove(account)
    accounts.remove(account)
    return jsonify({'message': '{} you have deleted your account, until next time '.format(account_name)})


@app.route('/task/<int:account_id>', methods=['POST'])
def create_task(account_id):
    account = search_account_by_id(account_id)
    if account not in logged_in_accounts:
        return jsonify({'message': 'Please Login before you can access the account'})
    data = request.json
    task_name = data.get('task_name')
    if not task_name:
        return jsonify({'message': 'Please fill in task name'})
    if not isinstance(task_name, str):
        return jsonify({'message': 'Task name should be in alphabetical characters'})
    if not task_name.isalpha():
        return jsonify({'message': 'Task name should be in alphabetical characters'})
    if task_name in [task.task_name for task in tasks if task.account_id == account_id]:
        return jsonify({'message': 'Task name already exists'})
    task_id = max([task.task_id for task in tasks]) + 1 if tasks else 1
    task = Task(task_id, task_name, account_id)
    tasks.append(task)
    return jsonify({'message': '{} of ID {} task has been created'.format(task.task_name, task.task_id)})


@app.route('/task/<int:account_id>/delete/<int:task_id>', methods=['DELETE'])
def delete_task(account_id, task_id):
    account = search_account_by_id(account_id)
    if account not in logged_in_accounts:
        return jsonify({'message': 'Please Login before you can access the account'})
    if task_id not in [task.task_id for task in tasks if task.account_id == account_id]:
        return jsonify({'message': 'Task does not exist'})
    task = search_task_by_id(task_id)
    task_name = task.task_name
    deleted_tasks.append(task)
    tasks.remove(task)
    return jsonify({'message': '{} task has been deleted'.format(task_name)})


@app.route('/task/<int:account_id>/delete', methods=['DELETE'])
def delete_all_tasks(account_id):
    account = search_account_by_id(account_id)
    if account not in logged_in_accounts:
        return jsonify({'message': 'Please Login before you can access the account'})
    my_tasks = [task for task in tasks if task.account_id == account_id]
    if not my_tasks:
        return jsonify({'message': 'You have no tasks'})
    for task in tasks:
        deleted_tasks.append(task)
    my_tasks.clear()
    return jsonify({'message': 'All tasks have been successfully deleted'})


@app.route('/task/<int:account_id>/delete/<int:task_id>/recover', methods=['GET'])
def recover(account_id, task_id):
    account = search_account_by_id(account_id)
    if not account:
        return jsonify({'message': 'Please Login before you can access the account'})
    if account not in logged_in_accounts:
        return jsonify({'message': 'Please Login before you can access the account'})
    if task_id not in [task.task_id for task in deleted_tasks if task.account_id == account_id]:
        return jsonify({'message': 'Task does not exist'})
    task = [task for task in deleted_tasks if task_id == task.task_id][0]
    tasks.append(task)
    return jsonify({'message': '{} has been recovered successfully'.format(task.task_name)})


@app.route('/task/<int:account_id>/mark/<int:task_id>', methods=['PUT'])
def mark_task(account_id, task_id):
    account = search_account_by_id(account_id)
    if account not in logged_in_accounts:
        return jsonify({'message': 'Please Login before you can access the account'})
    task = search_task_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task does not exist'})
    if task.marked is True:
        return jsonify({'message': 'Task is already marked'})
    data = request.json
    marked = data.get('marked')
    if not marked:
        return jsonify({'message': 'Please fill in task name'})
    if marked != "True":
        return jsonify({'message': 'Please enter True to mark a task'})
    task.marked = bool(marked)
    return jsonify({'message': '{} has been marked'.format(task.task_name)})


@app.route('/task/<int:account_id>/unmark/<int:task_id>', methods=['PUT'])
def un_mark_task(account_id, task_id):
    account = search_account_by_id(account_id)
    if account not in logged_in_accounts:
        return jsonify({'message': 'Please Login before you can access the account'})
    task = search_task_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task does not exist'})
    if task.marked is False:
        return jsonify({'message': 'Task is already marked'})
    data = request.json
    marked = data.get('marked')
    if not marked:
        return jsonify({'message': 'Please fill in task name'})
    if marked != "False":
        return jsonify({'message': 'Please enter False to mark a task'})
    task.marked = bool(marked)
    return jsonify({'message': '{} has been unmarked'.format(task.task_name)})


if __name__ == '__main__':
    app.run()
