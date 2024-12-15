from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz, lang, products
from datetime import datetime
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
    println_colored(f"{lang['welcome']} {user['name']}!", Color.GREEN)
    while True:
        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {lang['product_list']}", Color.CYAN)
        println_colored(f"2 -> {lang['my_balance']}", Color.CYAN)
        println_colored(f"3 -> {lang['add_balance']}", Color.CYAN)  # Balans qo'shish
        println_colored(f"4 -> {lang['buy_product']}", Color.CYAN)
        println_colored(f"5 -> {lang['expensive_product_list']}", Color.CYAN)
        println_colored(f"6 -> {lang['my_products']}", Color.CYAN)
        println_colored(f"7 -> {lang['my_profile']}", Color.CYAN)
        println_colored(f"8 -> {lang['edit_profile']}", Color.CYAN)
        println_colored(f"9 -> {lang['search_product']}", Color.CYAN)
        println_colored(f"10 -> {lang['favorite_product']}", Color.CYAN)
        println_colored(f"11 -> {lang['delete_account']}", Color.CYAN)
        println_colored(f"12 -> {lang['contact_admin']}", Color.CYAN)
        println_colored(f"13 -> {lang['exit_account']}", Color.CYAN)
        println_colored("==================================", Color.DARK_ORANGE)

        choose = input(lang['choice'])

        if choose == '1':
            productList(user_id)
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
            searchProduct()
        elif choose == '10':
            favoriteProduct(user_id)
        elif choose == '11':
            confirm = input(f"{lang['confirm_removal_account']} (y/n): ").strip().lower()
            if confirm == 'y':
                display_loading_animation(lang['loading'], Color.CYAN)
                if delete_account(user_id):
                    println_colored(f"{lang['account_deleted']}", Color.GREEN)
                    return
            else:
                println_colored(lang['removal_cancelled'], Color.RED)
        elif choose == '12':
            contact_admin(user_id)
        elif choose == '13':
            confirm = input(f"{lang['confirm_logout']} (y/n): ").strip().lower()
            if confirm == 'y':
                display_loading_animation(lang['loading'], Color.CYAN)
                println_colored(f"{lang['account_exited']}", Color.GREEN)
                return
            else:
                println_colored(lang['action_cancelled'], Color.RED)
        else:
            println_colored(lang['invalid_choice'], Color.RED)


def send_message_to_admin(user_id, title, description):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        admin_info['messages'].append({
            "title": title,
            "description": description,
            "from": {
                "id": user['id'],
                "name": user['name'],
                "login": user['login']
            },
            "to": {
                "id": admin_info['admin_login'],
                "role": "admin"
            }
        })
        println_colored(f"{lang['message_sent']}: {title} | {description}", Color.GREEN)
    else:
        println_colored(f"{lang['user_not_found']}.", Color.RED)


def contact_admin(user_id):
    while True:
        print(f"\n1. {lang['message_to_admin']}")
        print(f"2. {lang['admin_answers']}")
        print(f"3. {lang['back']}")

        choice = input(f"{lang['choice']}")

        if choice == "1":
            title = input(f"{lang['enter_message_title']}:")
            description = input(f"{lang['enter_message_description']}: ")
            send_message_to_admin(user_id, title, description)
        elif choice == "2":
            user_messages = users[user_id - 1].get('messages', [])
            if user_messages:
                println_colored(f"{users[user_id - 1]['name']} {lang['replies_admin']}:")
                for msg in user_messages:
                    from_name = msg['from']['name']
                    message = msg['description']  # Assuming description is the message body
                    println_colored(f"{from_name} {lang['answer']}: {message}", Color.CYAN)
            else:
                println_colored(f"{lang['no_messages']}", Color.YELLOW)

        elif choice == "3":
            print(f"{lang['back']}")
            break
        else:
            println_colored(f"{lang['invalid_choice']}", Color.RED)


def delete_account(user_id):
    global users, products
    user_to_delete = None

    for user in users:
        if user["id"] == user_id:
            user_to_delete = user
            break

    if user_to_delete:
        deleted_user_id = user_to_delete["id"]

        users.remove(user_to_delete)

        for product in products:
            product["comments"] = [comment for comment in product["comments"] if comment["user_id"] != deleted_user_id]

        return True
    else:
        return False


def get_user_favorites(user_id):
    for user in users:
        if user["id"] == user_id:
            favorite_products = []

            for fav in user["favoriteProducts"]:
                product_id = fav["id"]

                for product in products:
                    if product["id"] == product_id:
                        favorite_products.append(product)

            return favorite_products

    return []


def favoriteProduct(user_id):
    favorites = get_user_favorites(user_id)

    while True:
        println_colored("==================================", Color.DARK_ORANGE)

        if not favorites:
            println_colored(f"{lang['you_dont_have_favorites']}", Color.RED)
        else:
            println_colored(f"{lang['products']}:", Color.CYAN)
            for product in favorites:
                print(f"- {product['name']} (ID: {product['id']})")

        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {lang['remove_from_favorite']}", Color.CYAN)
        println_colored(f"2 -> {lang['back']}", Color.CYAN)
        println_colored("==================================", Color.DARK_ORANGE)

        choice = input(f"{lang['choice']}")

        if choice == '1':
            product_id = input(f"{lang['enter_product_id']}: ")
            removeFromFavorites(user_id, product_id)

        elif choice == '2':
            break

        else:
            println_colored(f"{lang['invalid_choice']}", Color.RED)


def removeFromFavorites(user_id, product_id):
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if not user:
        println_colored(f"{lang['user_not_found']}", Color.RED)
        return
    if not product:
        println_colored(f"{lang['product_not_found']}", Color.RED)
        return

    if product not in user["favoriteProducts"]:
        println_colored(f"{lang['product_not_found']}.", Color.RED)
        return

    user["favoriteProducts"].remove(product)
    println_colored(f"{lang['remove_from_favorites']}", Color.GREEN)


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

    println_colored(
        f"{lang['current_profile']}:\n{lang['name']}: {user['name']}\n{lang['login']}: {user['login']}\n{lang['balance']}: {user['balance']}\n",
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
        println_colored(
            f"{lang['name']}: {user['name']} | {lang['login']}: {user['login']} | {lang['password']} : {user['password']} | {lang['balance']}: {user['balance']}",
            Color.DARK_ORANGE)
        println_colored("============================================================", Color.CYAN)
    else:
        println_colored(f"{lang['no_users_found']}", Color.RED)


def myProducts(user_id):
    display_loading_animation(lang['loading'], Color.MAGENTA)
    user = get_user_by_id(user_id)
    if user:
        myProducts = user.get("myProducts", [])
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
    println_colored(f"========================== {lang['expensive_product_list']} ==========================",
                    Color.YELLOW)
    filtered_products = sorted(products, key=lambda product: product['product_price'], reverse=True)
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
            println_colored(
                f"ID: {product['id']} -> {product['product_name']} | {lang['price']}: {product['product_price']}",
                Color.GREEN)

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


def productList(user_id):
    display_loading_animation(lang['loading'], Color.MAGENTA)
    while True:
        if not products:
            println_colored(lang['no_products'], Color.RED)
        else:
            println_colored(f"========================== {lang['products']} ==========================", Color.CYAN)
            for product in products:
                println_colored(
                    f"ID: {product['id']} {lang['name']}: {product['product_name']} | {lang['price']}: {product['product_price']} | {lang['date']}: {product['product_date']}",
                    Color.DARK_ORANGE)

            println_colored("============================================================", Color.CYAN)
            print(f"\n1. {lang['add_to_favorites']}")
            print(f"2. {lang['product_details']}")
            print(f"3. {lang['back']}")

            action = input(lang["choice"])

            if action == "1":
                product_id = int(input(lang["enter_product_id"]))
                addToFavorites(user_id, product_id)
            elif action == '2':
                product_id = int(input(lang["enter_product_id"]))
                productDetail(product_id=product_id, user_id=user_id)
            elif action == "3":
                return
            else:
                println_colored(lang["invalid_choice"], Color.RED)


def productDetail(product_id, user_id):
    display_loading_animation(f'{lang["loading"]}', Color.YELLOW)
    while True:
        product = None
        for p in products:
            if p["id"] == product_id:
                product = p
                break

        if not product:
            print(f"{lang['product_not_found']}!")
            return

        println_colored(f"\n==== {lang['product_detail']} ====", Color.DARK_ORANGE)
        print(f"{lang['name']}: {product['product_name']}")
        print(f"{lang['price']}: {product['product_price']}")
        print(f"{lang['date']}: {product['product_date']}")

        println_colored(f"\n{lang['comments']}:", Color.YELLOW)
        if len(product["comments"]) == 0:  # Correctly check if there are no comments
            println_colored(f"{lang['no_comments']}", Color.MAGENTA)
        else:
            for idx, comment in enumerate(product["comments"], start=1):
                print(f"{idx}. {comment['login']} ({comment['date']}): {comment['text']}")

        print(f"\n1. {lang['add_comment']}")
        print(f"2. {lang['remove_comment']}")
        print(f"3. {lang['back']}")

        action = input(f"{lang['choice']} ")
        if action == "1":
            addComment(user_id, product_id)
        elif action == "2":
            comment_index = input(f"{lang['input_comment_id']}: ")
            if comment_index.isdigit():
                removeComment(product_id, int(comment_index) - 1, user_id)
            else:
                println_colored(f"{lang['invalid_index']}", Color.RED)
        elif action == "3":
            return
        else:
            println_colored(f"{lang['invalid_choice']}", Color.RED)


def addComment(user_id, product_id):
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if not product:
        println_colored(f"{lang['product_not_found']}!", Color.RED)
        return

    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    if not user:
        println_colored(f"{lang['user_not_found']}!", Color.RED)
        return

    comment_text = input(f"{lang['input_comment']} ").strip()
    if not comment_text:
        println_colored(f"{lang['comment_empty']}", Color.RED)
        return

    # Add the comment
    comment = {
        "login": user["login"],
        "date": get_current_date(),
        "text": comment_text
    }
    product["comments"].append(comment)
    println_colored(f"{lang['comment_added_successfully']}", Color.GREEN)


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def removeComment(product_id, comment_index, user_id):
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if not product:
        println_colored(f"{lang['product_not_found']}!", Color.RED)
        return

    if comment_index < 0 or comment_index >= len(product["comments"]):
        println_colored(f"{lang['invalid_index']}", Color.RED)
        return

    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    if not user:
        println_colored(f"{lang['user_not_found']}!", Color.RED)
        return

    # userni commenti ekanligiga tekshirish
    comment = product["comments"][comment_index]
    if comment["login"] != user["login"]:
        println_colored(f"{lang['cannot_delete_others_comment']}", Color.RED)
        return

    removed_comment = product["comments"].pop(comment_index)
    println_colored(f"{lang['comment_removed']}: {removed_comment['text']}", Color.GREEN)


def addToFavorites(user_id, product_id):
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u
            break

    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if not user:
        println_colored(f"{lang['user_not_found']}", Color.RED)
        return
    if not product:
        println_colored(f"{lang['product_not_found']}", Color.RED)
        return

    if product in user["favoriteProducts"]:
        println_colored(f"{lang['already_favorites']}.", Color.RED)
        return

    user["favoriteProducts"].append(product)
    println_colored(f"{lang['add_to_favorites']}", Color.DARK_ORANGE)


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
