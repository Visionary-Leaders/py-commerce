from utils.util import println_colored, Color
from data.local_data import eng, uz
from data.main_func import signIn, signUp


def initMain():
    global lang
    while True:
        println_colored(f"1.{lang['signin']}", Color.GREEN)
        println_colored(f"2.{lang['signUp']}", Color.CYAN)
        println_colored(f"3.{lang['lang']}", Color.MAGENTA)
        println_colored("==================================", Color.DARK_ORANGE)
        choose = input(lang['choice'])
        if choose == '1':
            login = input(lang['input_login'] + ":")
            password = input(lang['input_password'] + ":")
            signIn(login, password)
        elif choose == '2':
            name = input(f"{lang['name']}:")
            password = input(f"{lang['input_password']}:")
            login = input(f"{lang['input_login']}:")
            signUp(name, password, login)

        elif choose == '3':
            println_colored("==================================", Color.BLUE)
            print("1.uz 2.eng")
            choose = input(lang['choice'])
            if choose == '1':
                lang = uz
            elif choose == '2':
                lang = eng
            else:
                println_colored(lang['invalid_choice'], Color.RED)
        else:
            println_colored(lang['invalid_choice'], Color.RED)


initMain()
