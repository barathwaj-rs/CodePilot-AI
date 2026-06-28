
import auth

def login_user(username, password):
    # your existing authentication logic here
    if authenticated:
        token = auth.generate_token(username)
        return {'token': token}
    else:
        return {'error': 'Invalid credentials'}, 401
