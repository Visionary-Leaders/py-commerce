from data.local_data import users

def checkUser(login1, password1):
    # USer mavjud mavjud emasligiga tekshiradi
    for user in users:
        if user["login"] == login1 and user["password"] == password1:
            return True
    return False


def getUserId(login, password):
    for user in users:
        if user["login"] == login and user["password"] == password:
            return user['id']
    return -1
