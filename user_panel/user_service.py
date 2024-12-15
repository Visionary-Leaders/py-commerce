from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz, lang,products
from admin_panel.admin_data import checkUserAdmin, admin_info
from user_panel.user_data import users, checkUser, getUserId

# ######################### User Page ####################
# User Page ->
# Product List
# My Balance
# Buy Product
# expensiveProductList
# myProductList
# My Profile
# Edit Profile
# Search Product
# FavoriteProduct
# Delete Account
# Contact Admin  // Soon
# Exit Account

def userPage(user_id):
    user = get_user_by_id(user_id)
    balance = user["balance"]
    println_colored(f"{lang['welcome']} {user['name']}!", Color.GREEN)
    while True:
        user = get_user_by_id(user_id)

        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {lang['product_list']}", Color.MAGENTA)
        println_colored(f"2 -> {lang['my_balance']}", Color.MAGENTA)
        println_colored(f"3 -> {lang['add_balance']}", Color.MAGENTA)  # Balans qo'shish
        println_colored(f"4 -> {lang['buy_product']}", Color.MAGENTA)
        println_colored(f"5 -> {lang['expensive_product_list']}", Color.MAGENTA)
        println_colored(f"6 -> {lang['my_products']}", Color.MAGENTA)
        println_colored(f"7 -> {lang['my_profile']}", Color.MAGENTA)
        println_colored(f"8 -> {lang['edit_profile']}", Color.MAGENTA)
        println_colored(f"9 -> {lang['search_product']}", Color.MAGENTA)
        println_colored(f"10 -> {lang['favorite_product']}", Color.MAGENTA)
        println_colored(f"11 -> {lang['delete_account']}", Color.MAGENTA)
        println_colored(f"12 -> {lang['contact_admin']}", Color.MAGENTA)
        println_colored(f"13 -> {lang['exit_account']}", Color.MAGENTA)
        println_colored("==================================", Color.DARK_ORANGE)

        choose = input(lang['choice'])

        if choose == '1':
            productList()
        elif choose == '2':
            myBalance(user_id)
        elif choose == '3':
            addBalance(user_id)
        elif choose == '4':
            buyProduct(user_id)
        elif choose == '5':
            sortExpensiveProduct()
        elif choose == '6':
            myProducts(user_id)
        elif choose == '7':
            myProfile(user_id)
        elif choose == '8':
            editProfile(user_id)
        elif choose == '9':
            pass
        elif choose == '10':
            pass
        elif choose == '11':
            pass
        elif choose == '12':
           pass
        elif choose == '13':
            pass
        else:
            println_colored(lang['invalid_choice'], Color.RED)

def checkLoginExists(new_login):
    return any(user["login"] == new_login for user in users)


def editProfile(user_id):
    display_loading_animation(lang['loading'], Color.MAGENTA)
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    if not user:
        println_colored(lang['user_not_found'], Color.RED)
        return

    println_colored(f"{lang['current_profile']}:\n{lang['name']}: {user['name']}\n{lang['login']}: {user['login']}\n{lang['balance']}: {user['balance']}\n",
                    Color.BLUE)

    println_colored(lang['edit_name_prompt'], Color.GREEN)
    new_name = input(lang['new_name'])
    if new_name:
        user['name'] = new_name
        println_colored(f"{lang['name_updated_to']}: {user['name']}", Color.GREEN)

    println_colored(lang['edit_login_prompt'], Color.GREEN)
    new_login = input(lang['new_login'])
    if new_login:
        if checkLoginExists(new_login):
            println_colored(lang['login_taken'], Color.RED)
        else:
            user['login'] = new_login
            println_colored(f"{lang['login_updated_to']}: {user['login']}", Color.GREEN)

    println_colored(lang['edit_password_prompt'], Color.GREEN)
    new_password = input(lang['new_password'])
    if new_password:
        confirm_password = input(lang['confirm_password'])
        if new_password == confirm_password:
            user['password'] = new_password
            println_colored(f"{lang['password_updated']}", Color.GREEN)
        else:
            println_colored(lang['password_mismatch'], Color.RED)

    println_colored(f"{lang['profile_updated']}", Color.GREEN)


def myProfile(user_id):
    display_loading_animation(lang['loading'], Color.MAGENTA)
    user = get_user_by_id(user_id)
    if user:
        println_colored(f"========================== {lang['my_profile']} ==========================", Color.CYAN)
        println_colored(f"{lang['name']}: {user['name']} | {lang['login']}: {user['login']} | {lang['password']} : {user['password']} | {lang['balance']}: {user['balance']}", Color.DARK_ORANGE)
        println_colored("============================================================", Color.CYAN)
    else:
        println_colored(f"{lang['no_users_found']}", Color.RED)

def myProducts(user_id):
    display_loading_animation(lang['loading'], Color.MAGENTA)
    user = get_user_by_id(user_id)
    if user:
        myProducts = user["myProducts"]
        println_colored(f"========================== {lang['my_products']} ==========================", Color.CYAN)
        for product in myProducts:
            println_colored(
                f"ID: {product['id']} | {lang['name']}: {product['product_name']} | {lang['price']}: {product['product_price']} | {lang['date']}: {product['product_date']}",
                Color.DARK_ORANGE)
        println_colored("============================================================", Color.CYAN)
    else:
        println_colored(f"{lang['no_users_found']}", Color.RED)

def sortExpensiveProduct():
    display_loading_animation(lang['loading'], Color.MAGENTA)
    println_colored(f"========================== {lang['expensive_product_list']} ==========================", Color.YELLOW)
    filtered_products=sorted (products, key=lambda product: product['product_price'], reverse=True)
    for product in filtered_products:
        println_colored(
            f"ID: {product['id']} | {lang['name']}: {product['product_name']} | {lang['price']}: {product['product_price']} | {lang['date']}: {product['product_date']}",
            Color.DARK_ORANGE)
    println_colored("============================================================", Color.YELLOW)


def buyProduct(user_id):
    display_loading_animation(lang['loading'], Color.MAGENTA)
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    if not user:
        println_colored(lang['user_not_found'], Color.RED)
        return

    println_colored(lang['product_list'], Color.BLUE)
    for product in products:
        if product not in user["myProducts"]:
            println_colored(f"ID: {product['id']} -> {product['product_name']} | {lang['price']}: {product['product_price']}", Color.GREEN)

    product_id = input(lang['choice_product'])
    product = None
    for p in products:
        if str(p["id"]) == product_id:
            product = p
            break

    if not product:
        println_colored(lang['invalid_product'], Color.RED)
        return

    if user["balance"] < int(product["product_price"]):
        println_colored(lang['insufficient_balance'], Color.RED)
        return

    user["balance"] -= int(product["product_price"])
    println_colored(f"{lang['success_bought_product']} {lang['remaining_balance']} {user['balance']}", Color.GREEN)

    user["myProducts"].append(product)

    product["sold_count"] += 1


def productList():
    display_loading_animation(lang['loading'], Color.MAGENTA)  # Loading animatsiyasini ko'rsatish
    if not products:  # Mahsulotlar ro'yxati bo'sh bo'lsa
        println_colored(lang['no_products'], Color.RED)  # Mahsulotlar yo'qligi haqida xabar berish
    else:
        println_colored(f"========================== {lang['products']} ==========================", Color.CYAN)

        # Mahsulotlarni ro'yxatlash
        for product in products:
            println_colored(
                f"{lang['name']}: {product['product_name']} | {lang['price']}: {product['product_price']} | {lang['date']}: {product['product_date']}",
                Color.DARK_ORANGE)

        # Mahsulotlar ro'yxatini yakunlash
        println_colored("============================================================", Color.CYAN)

        # Qo'shimcha amallar uchun menyu
        print("\n1. Add to Favorites")
        print(f"2. {lang['back']}")

        action = input(lang["enter_action_choice"])  # Foydalanuvchidan amalni tanlashni so'rash
        if action == "1":
            product_id = int(input(lang["enter_product_id_for_action"]))  # Qaysi mahsulotni tanlashni so'rash
            # addToFavorites(product_id)  # Sevimlilarga qo'shish funksiyasini chaqirish
        elif action == "2":
            product_id = int(input(lang["enter_product_id_for_action"]))  # Qaysi mahsulotga izoh qo'shishni so'rash
            # addComment(product_id)  # Izoh qo'shish funksiyasini chaqirish
        elif action == "3":
            return  # Oldingi sahifaga qaytish
        else:
            println_colored(lang["invalid_action"], Color.RED)  # Yaroqsiz amal


def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def myBalance(user_id):
    display_loading_animation(lang['loading'], Color.MAGENTA)
    user = get_user_by_id(user_id)
    if user:
        balance = user["balance"]
        println_colored(f"{lang['your_current_balance']}: {balance}", Color.GREEN)
    else:
        println_colored(f"{lang['no_users_found']}", Color.RED)

def addBalance(user_id):
    user = get_user_by_id(user_id)
    if user:
            amount = int(input(f"{lang['enter_amount']} "))
            if amount > 0:
                user["balance"] += amount
                display_loading_animation(lang['loading'], Color.MAGENTA)
                println_colored(f"{lang['success_added_balance']}: {user['balance']}", Color.GREEN)
            else:
                println_colored(f"{lang['invalid_amount']}", Color.RED)

    else:
        println_colored(f"{lang['no_users_found']}", Color.RED)