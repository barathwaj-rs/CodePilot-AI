
from auth import generate_token, verify_token

def login(username):
    if username == 'admin':
        token = generate_token(username)
        return {'token': token.decode('utf-8')}
    else:
        return {'error': 'Invalid username'}
