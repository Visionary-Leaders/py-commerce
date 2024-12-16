from data.local_data import admin_info


def checkUserAdmin(login1, password1):

    if admin_info["admin_login"] == login1 and admin_info["admin_password"] == password1:
        return True
    return False


