from data.local_data import users

def checkUser(login, password):
    for user in users:
        if user["login"] == login and user["password"] == password:
            return True
    return False


def getUserId(login, password):
    for user in users:
        if user["login"] == login and user["password"] == password:
            return user['id']
    return -1
