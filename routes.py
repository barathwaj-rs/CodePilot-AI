
from flask import Flask, request, jsonify
from auth import login

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login_route():
    username = request.json.get('username')
    password = request.json.get('password')
    token = login(username, password)
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(debug=True)
