from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz,current_language
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
        println_colored(current_language['login_error'], Color.RED)


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
    if not checkUser(login, password) and not checkUserAdmin(login, password):
        users.append(user)
        userPage(user["id"])
    else:
        println_colored(current_language['register_error'], Color.RED)


def initMain():
    global current_language
    while True:
        println_colored(f"1.{current_language['signin']}", Color.GREEN)
        println_colored(f"2.{current_language['signUp']}", Color.CYAN)
        println_colored(f"3.{current_language['lang']}", Color.MAGENTA)
        println_colored("==================================", Color.DARK_ORANGE)
        choose = int(input(current_language['choice']))
        display_loading_animation(current_language['loading'], Color.BLUE)
        if choose == 1:
            login = input(current_language['input_login'] + ":")
            password = input(current_language['input_password'] + ":")
            signIn(login, password)
        elif choose == 2:
            name = input(f"{current_language['name']}:")
            password = input(f"{current_language['input_password']}:")
            login = input(f"{current_language['input_login']}:")
            signUp(name, password, login)

        elif choose == 3:
            println_colored("==================================", Color.BLUE)
            print("1.uz 2.eng")
            choose = int(input(current_language['choice']))
            if choose == 1:
                current_language = uz
            elif choose == 2:
                current_language = eng
            else:
                println_colored(current_language['invalid_choice'], Color.RED)
        else:
            println_colored(current_language['invalid_choice'], Color.RED)


initMain()
