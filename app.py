from flask import Flask, request, jsonify

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


if __name__ == '__main__':
    app.run()
