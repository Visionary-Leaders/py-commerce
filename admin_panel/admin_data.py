admin_info = {
    "admin_login": "superadmin",
    "admin_password": "1234",
    "role": "admin"
}


def checkUserAdmin(login, password):
    if login == admin_info["admin_login"] and password == admin_info["admin_password"]:
        return True
    return False
