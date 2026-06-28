
def handle_login(request):
    username = request['username']
    password = request['password']
    if 'login' in username and 'password' in password:
        result = login(username, password)
        return {'result': result}
    else:
        return {'result': ''}
