from data.local_data import admin_info


def checkUserAdmin(login, password):
    if login == admin_info["admin_login"] and password == admin_info["admin_password"]:
        return True
    return False
