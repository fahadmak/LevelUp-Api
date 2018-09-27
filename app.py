from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/auth/signup', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    username = data.get('username')
    password = data.get('password')
    return jsonify({'message': '{} you have successfully created an account'.format(username)})


if __name__ == '__main__':
    app.run()
