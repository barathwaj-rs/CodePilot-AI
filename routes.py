
from auth import login

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    token = login(username, password)
    if token:
        return {'token': token}
    else:
        return {'error': 'Invalid credentials'}
