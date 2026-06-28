
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your_secret_key_here'  # Replace with a secure secret key

def generate_token(username):
    payload = {'username': username, 'exp': datetime.utcnow() + timedelta(days=30)}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token.decode('utf-8')

def login(username, password):
    if username == 'admin' and password == 'your_password_here':
        return generate_token(username)
    else:
        return None
