
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'your_secret_key_here'

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token.decode('utf-8')

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return True
    except Exception as e:
        print(f"Error verifying token: {str(e)}")
        return False

