from admin_panel.admin_service import admin_page
from user_panel.user_data import checkUser, getUserId
from user_panel.user_service import userPage
from utils.util import println_colored, Color
from data.local_data import   users
from admin_panel.admin_data import checkUserAdmin


def signIn(login: str, password: str,language):
    if checkUserAdmin(login, password):
        admin_page(language)
    elif len(users) != 0 and checkUser(login, password):
        userPage(getUserId(login, password))
    else:
        println_colored(language['login_error'], Color.RED)


def signUp(name, password, login,lang):
    user = {
        "id": len(users) + 1,
        "name": name,
        "password": password,
        "login": login,
        "comments": [],
        "balance": 10000,
        "role": "user",
        "messages": [],
        "myProducts": [],
        "favoriteProducts": [], }
    if not checkUser(login, password) and not checkUserAdmin(login, password) and len(login) != 0 and len(
            password) != 0:
        users.append(user)
        userPage(user["id"],lang)
    else:
        println_colored(lang['register_error'], Color.RED)
