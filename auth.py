
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your_secret_key_here'

def create_token(username: str) -> str:
    payload = {'username': username, 'exp': datetime.utcnow() + timedelta(days=7)}
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def login(username: str) -> str:
    if username == 'admin':
        return create_token(username)
    else:
        raise Exception('Invalid username')
