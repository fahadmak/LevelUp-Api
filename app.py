from flask import Flask, request, jsonify
from api.auth.utils import search_account_by_username
from api.auth.model import accounts, Account, logged_in_accounts

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
    account_id = max([account.accountid for account in accounts]) + 1 if accounts else 1
    account = Account(account_id, name, username, password)
    accounts.append(account)
    return jsonify({'message': '{} you have successfully created an account'.format(username)})


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
    if account.password != password:
        return jsonify({'message': 'User name and password do not match'})
    for item in [username, password]:
        if not isinstance(item, str):
            return jsonify({'message': 'Please input correct information'})
    if account in logged_in_accounts:
        return jsonify({'message': 'You are already logged in'})
    logged_in_accounts.append(account)
    return jsonify({'message': '{} you have logged in'.format(username)})


if __name__ == '__main__':
    app.run()
