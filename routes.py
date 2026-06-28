
from flask import request, jsonify
import auth

@app.route('/protected', methods=['GET'])
def protected():
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'Unauthorized'}), 401
    
    token = request.headers['Authorization'].split(' ')[1]
    
    user_id = auth.verify_token(token)
    
    if user_id is None:
        return jsonify({'error': 'Invalid or expired token'}), 401
    
    # Access controlled resources here
            