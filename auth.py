
import jwt
from datetime import datetime, timedelta

def generate_token(username: str) -> str:
    payload = {"username": username, "exp": int(datetime.utcnow().replace(tzinfo=datetime.timezone.utc).timestamp()) + 3600}
    token = jwt.encode(payload, "your_secret_key", algorithm="HS256")
    return token.decode("utf-8")

def login(username: str, password: str) -> str:
    if username == "admin" and password == "password":
        return generate_token(username)
    else:
        raise ValueError("Invalid credentials")
