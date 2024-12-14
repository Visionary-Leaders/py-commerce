users = [
    {
        "id": 1,
        "name": "John Doe",
        "login": "john123",
        "password": "johnme",
        "messages": [],
        "balance": 0,  # No balance is needed for this example
        "myProducts": [],  # User's own products
        "favoriteProducts": []  # User's favorite products
    },
]


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
