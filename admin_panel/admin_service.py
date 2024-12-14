from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz, lang
from admin_panel.admin_data import checkUserAdmin, admin_info
from user_panel.user_data import users, checkUser, getUserId
from user_panel.user_service import userPage
from datetime import datetime

products = [
    {"id": 1, "product_name": "Laptop", "product_price": "1000", "product_date": "12/15/2024 10:30:45"},
    {"id": 2, "product_name": "Smartphone", "product_price": "500", "product_date": "12/16/2024 11:25:32"},
    {"id": 3, "product_name": "Tablet", "product_price": "300", "product_date": "12/17/2024 12:40:50"}
]


# ######################### Admin Page ####################
# Add Product
# Edit Product
# Most Sold Product
# Search Product
# All Product Price
# Message List // Soon
# User List
# Most buyer user a-z list
# Remove Product
# Ban User !
# log out
# Balance

def addProduct():
    productName = input(lang['product_name'] + ":")
    productPrice = input(lang['product_price'] + ":")
    current_time = datetime.now()
    productDate = current_time.strftime("%m/%d/%Y %H:%M:%S")
    products.append({
        "id": len(products) + 1,
        "product_name": productName,
        "product_price": productPrice,
        "product_date": productDate
    })
    display_loading_animation(lang['loading'], Color.CYAN)  # Dizayn uchun
    println_colored(lang['success_added_product'], Color.GREEN)


def editProduct():
    println_colored("========================== ProductList ==========================", Color.CYAN)
    for product in products:
        println_colored(
            f"ID: {product['id']} | {lang['name']}: {product['product_name']} | {lang['price']}: {product['product_price']} | {lang['date']}: {product['product_date']}",
            Color.DARK_ORANGE)
    println_colored("============================================================", Color.CYAN)

    product_id = int(input(lang['enter_product_id'] + ": "))
    selected_product = next((product for product in products if product['id'] == product_id), None)

    if selected_product:
        new_name = input(lang['edit_product_name'] + f" (current: {selected_product['product_name']}): ")
        new_price = input(lang['edit_product_price'] + f" (current: {selected_product['product_price']}): ")

        if new_name.strip():
            selected_product['product_name'] = new_name
        if new_price.strip():
            selected_product['product_price'] = new_price

        current_time = datetime.now()
        selected_product['product_date'] = current_time.strftime("%m/%d/%Y %H:%M:%S")

        display_loading_animation(lang['loading'], Color.CYAN)
        println_colored(lang['success_edited_product'], Color.GREEN)
    else:
        println_colored(lang['product_not_found'], Color.RED)


def maxPriceProduct():
    if len(products) == 0:
        println_colored(lang['no_products'], Color.RED)
        return

    most_sold = max(products, key=lambda product: float(product['product_price']))

    println_colored(
        f"ID: {most_sold['id']} | Name: {most_sold['product_name']} | Price: {most_sold['product_price']} | Date: {most_sold['product_date']}",
        Color.CYAN)


def mostSoldProduct():
    pass


def searchProduct():
    search_term = input(f"{lang['search_product_name']} : ").lower()
    found = False

    for product in products:
        if search_term in product['product_name'].lower():
            println_colored(
                f"ID: {product['id']} | {lang['name']}: {product['product_name']} | {lang['price']}: {product['product_price']} | {lang['date']}: {product['product_date']}",
                Color.DARK_ORANGE)
            found = True

    if not found:
        println_colored(lang['product_not_found'], Color.RED)


def messageToUser():
    println_colored("==================== Users ====================", Color.BLUE)
    for user in users:
        println_colored(f"ID: {user['id']} | {lang['name']}: {user['name']} | {lang['login']}: {user['login']}",
                        Color.CYAN)
    println_colored("===============================================", Color.BLUE)

    recipient_id = int(input(f"{lang['enter_recipent_id']} "))

    recipient = None
    for user in users:
        if user['id'] == recipient_id:
            recipient = user
            break

    if recipient:

        title = input(f"{lang['enter_message_title']}: ")
        message_description = input(f"{lang['enter_message_description']}: ")

        message = {
            "title": title,
            "description": message_description,
            "from": {"id": 0, "name": "SuperAdmin", "login": "super_admin"},  # Sender is the Admin
            "to": recipient  # Recipient user details
        }

        if 'messages' not in recipient:
            recipient['messages'] = []
        recipient['messages'].append(message)

        println_colored(f"{recipient['name']} {lang['message_sent_to']} !", Color.GREEN)
    else:
        println_colored(lang['user_not_found'], Color.RED)


def messageToMe():
    print(f"\n===== {lang['admin_inbox']} =====")

    if not admin_info['messages']:
        println_colored(f"{lang['no_message']}", Color.RED)
        return

    for message in admin_info['messages']:
        print("==================================")
        println_colored(f"{lang['message_from']}  {message['from']['name']} (ID: {message['from']['id']})", Color.CYAN)
        println_colored(f"{lang['enter_message_title']} {message['title']}", Color.CYAN)
        println_colored(f"{lang['enter_message_description']} {message['description']}", Color.CYAN)
        print("==================================")

def admin_page():
    while True:
        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {lang['add_product']}", Color.MAGENTA)
        println_colored(f"2 -> {lang['edit_product']}", Color.MAGENTA)
        println_colored(f"3 -> {lang['most_sold_product']}", Color.MAGENTA)
        println_colored(f"4 -> {lang['my_shop_balance']}", Color.MAGENTA)
        println_colored(f"5 -> {lang['search_product']}", Color.MAGENTA)
        println_colored(f"6 -> {lang['message_to_user']}", Color.MAGENTA)
        println_colored(f"7 -> {lang['message_to_me']}", Color.MAGENTA)
        println_colored(f"8 -> {lang['user_list']}", Color.MAGENTA)
        println_colored(f"9 -> {lang['most_buyer_user']}", Color.MAGENTA)
        println_colored(f"10 -> {lang['remove_product']}", Color.MAGENTA)
        println_colored(f"11 -> {lang['max_price_product']}", Color.MAGENTA)
        println_colored(f"12 -> {lang['log_out']}", Color.MAGENTA)
        println_colored("==================================", Color.DARK_ORANGE)
        choose = int(input(lang['choice']))
        if choose == 1:
            addProduct()
        elif choose == 2:
            editProduct()
        elif choose == 3:
            mostSoldProduct()
        elif choose == 4:
            pass
        elif choose == 5:
            searchProduct()
        elif choose == 6:
            messageToUser()
        elif choose == 7:
            messageToMe()
        elif choose == 8:
            pass
        elif choose == 9:
            pass
        elif choose == 10:
            pass
        elif choose == 11:
            maxPriceProduct()
        elif choose == 12:
            pass
        else:
            println_colored(lang["invalid_choice"], Color.RED)
