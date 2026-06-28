
from flask import request, jsonify
import auth

@app.route('/login', methods=['POST'])
def login_route():
    username = request.json['username']
    password = request.json['password']
    token = auth.login(username, password)
    if token:
        return jsonify({'token': token})
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
