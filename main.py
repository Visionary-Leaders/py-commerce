from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz,lang
from admin_panel.admin_data import checkUserAdmin, admin_info
from admin_panel.admin_service import admin_page
from user_panel.user_data import users, checkUser, getUserId
from user_panel.user_service import userPage



def signIn(login: str, password: str):
    if checkUserAdmin(login, password):
        admin_page()
    elif len(users) != 0 and checkUser(login, password):
        userPage(getUserId(login, password))
    else:
        println_colored(lang['login_error'], Color.RED)


def signUp(name, password, login):
    user = {
        "id": len(users) + 1,
        "name": name,
        "password": password,
        "login": login,
        "balance": 0,
        "role": "user",
        "messages": [],
        "my_products": [],
        "favorite_products": [], }
    if not checkUser(login, password) and not checkUserAdmin(login, password) and len(login) !=0 and len(password) !=0:
        users.append(user)
        userPage(user["id"])
    else:
        println_colored(lang['register_error'], Color.RED)


def initMain():
    global lang
    while True:
        println_colored(f"1.{lang['signin']}", Color.GREEN)
        println_colored(f"2.{lang['signUp']}", Color.CYAN)
        println_colored(f"3.{lang['lang']}", Color.MAGENTA)
        println_colored("==================================", Color.DARK_ORANGE)
        choose = int(input(lang['choice']))
        if choose == 1:
            login = input(lang['input_login'] + ":")
            password = input(lang['input_password'] + ":")
            signIn(login, password)
        elif choose == 2:
            name = input(f"{lang['name']}:")
            password = input(f"{lang['input_password']}:")
            login = input(f"{lang['input_login']}:")
            signUp(name, password, login)

        elif choose == 3:
            println_colored("==================================", Color.BLUE)
            print("1.uz 2.eng")
            choose = int(input(lang['choice']))
            if choose == 1:
                lang = uz
            elif choose == 2:
                lang = eng
            else:
                println_colored(lang['invalid_choice'], Color.RED)
        else:
            println_colored(lang['invalid_choice'], Color.RED)


initMain()
