users = [
    {
        "id": 1,
        "name": "John Doe",
        "login": "john123",
        "password": "johnme",
        "messages": [],
        "balance": 0,  # No balance is needed for this example
        "myProducts": [
            {"id": 1, "product_name": "Laptop", "product_price": "1000", "product_date": "12/15/2024 10:30:45"},
        ],  # User's own products
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
