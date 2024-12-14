admin_info = {
    "admin_login": "superadmin",
    "admin_password": "1234",
    'messages':[
        {
            "title": "Account Issue",
            "description": "I cannot log in to my account. Please assist.",
            "from": {
                "id": 1,
                "name": "John Doe",
                "login": "john123"
            },
            "to": {
                "id": "superadmin",
                "role": "admin"
            }
        },
    ],
    "role": "admin"
}


def checkUserAdmin(login, password):
    if login == admin_info["admin_login"] and password == admin_info["admin_password"]:
        return True
    return False
