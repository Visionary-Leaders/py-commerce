from utils.util import println_colored, Color
from data.local_data import eng
from data.local_data import uz

language =eng

while True:
    println_colored(f"1.{language['signin']}", Color.GREEN)
    println_colored(f"2.{language['signUp']}", Color.CYAN)
    println_colored(f"3.{language['lang']}", Color.MAGENTA)
    choose = int(input(language['choice']))
    if choose == 1:
        pass
    elif choose == 2:
        pass
    elif choose == 3:
        pass
    else:
        print(language['invalid_choice'])
