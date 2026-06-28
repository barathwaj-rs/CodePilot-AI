
import jwt
from datetime import datetime, timedelta

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(days=7)
    }
    return jwt.encode(payload, 'secret_key', algorithm='HS256')

def verify_token(token):
    try:
        decoded_token = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        return decoded_token
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

