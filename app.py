from flask import Flask, request, jsonify

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
    return jsonify({'message': '{} you have successfully created an account'.format(username)})


@app.route('/auth/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    return jsonify({'message': '{} you have successfully created an account'.format(username)})


if __name__ == '__main__':
    app.run()
