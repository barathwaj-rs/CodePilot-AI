
import jwt
from datetime import datetime

def generate_token(user_id: str) -> str:
    secret_key = os.environ['SECRET_KEY']
    payload = {'user_id': user_id, 'exp': datetime.utcnow() + timedelta(minutes=30)}
    return jwt.encode(payload, secret_key, algorithm='HS256')

def verify_token(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, os.environ['SECRET_KEY'], algorithms=['HS256'])
        return {'user_id': decoded_token['user_id']}
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def login(user_id: str) -> str:
    token = generate_token(user_id)
    return token
            