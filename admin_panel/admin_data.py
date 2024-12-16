from data.local_data import admin_info


def checkUserAdmin(login, password):
    if admin_info["admin_login"] == login and admin_info["admin_password"] == password:
        return True
    return False


