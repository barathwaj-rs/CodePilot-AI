
import jwt
from datetime import datetime
from flask import current_app

def login(username, password):
    if username == 'admin' and password == 'password':
        payload = {'user_id': 1}
        token = jwt.encode({'exp': datetime.utcnow() + datetime.timedelta(minutes=30), **payload}, 
                           current_app.config['SECRET_KEY'], algorithm='HS256')
        return token.decode('utf-8')
    else:
        return None
