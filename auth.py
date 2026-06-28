
import jwt
from datetime import datetime, timedelta

def generate_token(username):
    payload = {"username": username, "exp": (datetime.utcnow() + timedelta(hours=1)).isoformat()}
    return jwt.encode(payload, "secret_key", algorithm="HS256")

def login(username: str, password: str) -> str:
    if not authenticate_user(username, password):  # Replace with your authentication logic
        raise Exception("Invalid credentials")
    return generate_token(username)
