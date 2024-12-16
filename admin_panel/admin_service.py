from utils.util import println_colored, Color, display_loading_animation
from data.local_data import lang, products
from admin_panel.admin_data import admin_info
from user_panel.user_data import users
from datetime import datetime

removed_products = []


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
    # { id :automatic, productNomi ,productNarxi, productVaqti, sotilganlarSoni }
    productName = input(lang['product_name'] + ":")
    productPrice = input(lang['product_price'] + ":")
    current_time = datetime.now()
    productDate = current_time.strftime("%m/%d/%Y %H:%M:%S")
    products.append({
        "id": len(products) + 1,
        "product_name": productName,
        "product_price": productPrice,
        "product_date": productDate,
        "sold_count": 0,
    })
    display_loading_animation(lang['loading'], Color.CYAN)  # Dizayn uchun
    println_colored(lang['success_added_product'], Color.GREEN)


def showProducts():
    ## List Product )
    println_colored(f"========================== {lang['products']} ==========================", Color.CYAN)
    for product in products:
        println_colored(
            f"ID: {product['id']} | {lang['name']}: {product['product_name']} | {lang['price']}: {product['product_price']} | {lang['date']}: {product['product_date']}",
            Color.DARK_ORANGE)
    println_colored("============================================================", Color.CYAN)


def editProduct():
    showProducts()
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
    display_loading_animation(f"{lang['loading']}", Color.YELLOW)
    if not products:
        println_colored(lang['no_products'], Color.RED)
        return

    valid_products = []
    for product in products:
        if product.get('sold_count', 0) > 0:
            valid_products.append(product)

    if not valid_products:
        println_colored(f"{lang['no_products']}", Color.RED)
        return

    most_sold_product = max(valid_products, key=lambda product: product.get('sold_count', 0))

    println_colored(
        f"{lang['most_sold_product']}: ID: {most_sold_product['id']} | {lang['name']}: {most_sold_product['product_name']} | {lang['sold_count']}: {most_sold_product.get('sold_count', 0)}",
        Color.CYAN
    )


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

    recipient = next((user for user in users if user['id'] == recipient_id), None)

    if recipient:
        title = input(f"{lang['enter_message_title']}: ")
        message_description = input(f"{lang['enter_message_description']}: ")

        message = {
            "title": title,
            "description": message_description,
            "from": {"id": 0, "name": "SuperAdmin", "login": "super_admin"},
            "to": recipient
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


def userList():
    display_loading_animation(lang['loading'], Color.MAGENTA)
    println_colored("==================== Users ====================", Color.BLUE)
    for user in users:
        println_colored(f"ID: {user['id']} | {lang['name']}: {user['name']} | {lang['login']}: {user['login']}",
                        Color.CYAN)
    println_colored("===============================================", Color.BLUE)


def mostActiveUser():
    display_loading_animation(lang['loading'], Color.CYAN)
    if not users:
        println_colored(lang['no_users_found'], Color.RED)
        return None
    display_loading_animation(lang['loading'], Color.YELLOW)
    most_active_user = max(users, key=lambda user: len(user.get('myProducts', [])))
    product_count = len(most_active_user.get('myproducts', []))
    if product_count == 0:
        println_colored(lang['no_users_found'], Color.RED)
        return None
    println_colored(f"{lang['most_active_users']}: {most_active_user['name']} | {lang['products']}: {product_count}",
                    Color.CYAN)


def removeProduct():
    showProducts()
    product_id = int(input(lang['enter_product_id'] + ": "))
    selected_product = next((product for product in products if product['id'] == product_id), None)

    if selected_product:
        confirm = input(f"{lang['confirm_removal']} (y/n): ").strip().lower()
        if confirm == 'y':
            products.remove(selected_product)
            removed_products.append(selected_product)
            display_loading_animation(lang['loading'], Color.CYAN)
            println_colored(lang['success_removed_product'], Color.GREEN)
        else:
            println_colored(lang['removal_cancelled'], Color.YELLOW)
    else:
        println_colored(lang['product_not_found'], Color.RED)


def removedProducts():
    if not removed_products:
        println_colored(lang['no_products'], Color.RED)
    else:
        showProducts()
        print("\n1. " + lang['restore_product'])
        print("2. " + lang['clear_removed_products'])
        print("3. " + lang['back'])
        choice = input(lang['choice'] + ": ").strip()

        if choice == '1':
            product_id = int(input(lang['enter_product_id'] + ": "))
            selected_product = next((product for product in removed_products if product['id'] == product_id), None)
            if selected_product:
                removed_products.remove(selected_product)
                products.append(selected_product)
                println_colored(lang['product_restored'], Color.GREEN)
            else:
                println_colored(lang['product_not_found'], Color.RED)

        elif choice == '2':
            confirm = input(f"{lang['confirm_clear_removed']} (y/n): ").strip().lower()
            if confirm == 'y':
                removed_products.clear()
                println_colored(lang['removed_products_cleared'], Color.GREEN)
            else:
                println_colored(lang['action_cancelled'], Color.YELLOW)

        elif choice == '3':
            println_colored(lang['back_to_menu'], Color.YELLOW)

        else:
            println_colored(lang['invalid_choice'], Color.RED)


def productList():
    if not products:
        println_colored(lang['no_products'], Color.RED)
    else:
        showProducts()


def myShopBalance():
    display_loading_animation(lang['loading'], Color.CYAN)
    if len(users) == 0:
        println_colored(lang['no_users_found'], Color.RED)
    else:
        balance = 0
        for user in users:
            userProducts = user.get('myProducts')
            for product in userProducts:
                balance += product['product_price']
        println_colored(f"{lang['my_shop_balance']}: {balance}", Color.CYAN)


def admin_page():
    while True:
        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {lang['product_list']}", Color.MAGENTA)
        println_colored(f"2 -> {lang['add_product']}", Color.MAGENTA)
        println_colored(f"3 -> {lang['edit_product']}", Color.MAGENTA)
        println_colored(f"4 -> {lang['most_sold_product']}", Color.MAGENTA)
        println_colored(f"5 -> {lang['my_shop_balance']}", Color.MAGENTA)
        println_colored(f"6 -> {lang['search_product']}", Color.MAGENTA)
        println_colored(f"7 -> {lang['message_to_user']}", Color.MAGENTA)
        println_colored(f"8 -> {lang['message_to_me']}", Color.MAGENTA)
        println_colored(f"9 -> {lang['user_list']}", Color.MAGENTA)
        println_colored(f"10 -> {lang['most_buyer_user']}", Color.MAGENTA)
        println_colored(f"11 -> {lang['remove_product']}", Color.MAGENTA)
        println_colored(f"12 -> {lang['removed_products']}", Color.MAGENTA)
        println_colored(f"13 -> {lang['max_price_product']}", Color.MAGENTA)
        println_colored(f"14 -> {lang['log_out']}", Color.MAGENTA)
        println_colored("==================================", Color.DARK_ORANGE)
        choose = input(lang['choice'])
        if choose == '1':
            productList()
        elif choose == '2':
            addProduct()
        elif choose == '3':
            editProduct()
        elif choose == '4':
            mostSoldProduct()
        elif choose == '5':
            myShopBalance()
        elif choose == '6':
            searchProduct()
        elif choose == '7':
            messageToUser()
        elif choose == '8':
            messageToMe()
        elif choose == '9':
            userList()
        elif choose == '10':
            mostActiveUser()
        elif choose == '11':
            removeProduct()
        elif choose == '12':
            removedProducts()
        elif choose == '13':
            maxPriceProduct()
        elif choose == '14':
            confirm = input(f"{lang['confirm_logout']} (y/n): ").strip().lower()
            if confirm == 'y':
                display_loading_animation(lang['loading'], Color.CYAN)
                println_colored(f"{lang['account_exited']}", Color.GREEN)
                return
            else:
                println_colored(lang['action_cancelled'], Color.RED)

        else:
            println_colored(lang["invalid_choice"], Color.RED)
