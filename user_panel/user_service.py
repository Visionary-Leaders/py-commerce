from utils.util import println_colored, Color, display_loading_animation
from datetime import datetime
from admin_panel.admin_data import admin_info
from data.local_data import users, products, admin_info
from user_panel.user_data import users, getUserId


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

language ={}

def getUserById(user_id):
   found = None
   for user in users:
       if user ["id"] == user_id:
           found = user
           break

   return found

def getProductById(product_id):
    id = int(product_id)
    product = None
    for p in products:
        if p["id"] == id:
            product = p
            break
    return product


def send_message_to_admin(user_id, title, description):
    # Message To Admin  { kimdan { id ism login } kimga { admin,id, }
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
        println_colored(f"{language['message_sent']}: {title} | {description}", Color.GREEN)
    else:
        println_colored(f"{language['user_not_found']}.", Color.RED)


def contact_admin(user_id):
    while True:
        # Chatting Adming  (:)
        print(f"\n1. {language['message_to_admin']}")
        print(f"2. {language['admin_answers']}")
        print(f"3. {language['back']}")
        choice = input(f"{language['choice']}")

        # Adminga xabar yuborish
        if choice == "1":
            title = input(f"{language['enter_message_title']}:")
            description = input(f"{language['enter_message_description']}: ")
            send_message_to_admin(user_id, title, description)
        # Admindan kelgan xabar
        elif choice == "2":
            #  user_message = users[index]['messages] { messageIsm,description, kimdan {superadmmin,id }
            # kimga { myId,myLogin }
            user_messages = users[user_id - 1].get('messages', [])
            if user_messages:
                println_colored(f"{users[user_id - 1]['name']} {language['replies_admin']}:")
                for msg in user_messages:
                    from_name = msg['from']['name']  ##Kimdan ligi   :superadmin
                    message = msg['description']  # DEscription )
                    println_colored(f"{from_name} {language['answer']}: {message}", Color.CYAN)
            else:
                println_colored(f"{language['no_messages']}", Color.YELLOW)

        elif choice == "3":
            # just break )
            print(f"{language['back']}")
            break
        else:
            println_colored(f"{language['invalid_choice']}", Color.RED)


def delete_account(user_id):
    global users, products
    user_to_delete = getUserById(user_id)

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
            println_colored(f"{language['you_dont_have_favorites']}", Color.RED)
        else:
            println_colored(f"{language['products']}:", Color.CYAN)
            for product in favorites:
                print(f"- {product['name']} (ID: {product['id']})")

        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {language['remove_from_favorite']}", Color.CYAN)
        println_colored(f"2 -> {language['back']}", Color.CYAN)
        println_colored("==================================", Color.DARK_ORANGE)

        choice = input(f"{language['choice']}")

        if choice == '1':
            product_id = input(f"{language['enter_product_id']}: ")
            removeFromFavorites(user_id, product_id)

        elif choice == '2':
            break

        else:
            println_colored(f"{language['invalid_choice']}", Color.RED)


def removeFromFavorites(user_id, product_id):
    user = getUserById(user_id)

    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if not user:
        println_colored(f"{language['user_not_found']}", Color.RED)
        return
    if not product:
        println_colored(f"{language['product_not_found']}", Color.RED)
        return

    if product not in user["favoriteProducts"]:
        println_colored(f"{language['product_not_found']}.", Color.RED)
        return

    user["favoriteProducts"].remove(product)
    println_colored(f"{language['remove_from_favorites']}", Color.GREEN)


def searchProduct(user_id):
    search_term = input(f"{language['search_product_name']} : ").lower()
    found_product=None
    for product in products:
        if search_term in product['product_name'].lower():
            found_product=product
    if not found_product:
        println_colored(language['product_not_found'], Color.RED)
    else :
        productDetail(found_product['id'], user_id=user_id)

def checkLoginExists(new_login):
    return any(user["login"] == new_login for user in users)


def editProfile(user_id):
    display_loading_animation(language['loading'], Color.MAGENTA)
    user = getUserById(user_id=user_id)
    if not user:
        println_colored(language['user_not_found'], Color.RED)
        return

    println_colored(
        f"{language['current_profile']}:\n{language['name']}: {user['name']}\n{language['login']}: {user['login']}\n{language['balance']}: {user['balance']}\n",
        Color.BLUE)

    println_colored(language['edit_name_prompt'], Color.GREEN)

    # New Name
    new_name = input(language['new_name'])
    if new_name:
        user['name'] = new_name
        println_colored(f"{language['name_updated_to']}: {user['name']}", Color.GREEN)

    # New Login
    println_colored(language['edit_login_prompt'], Color.GREEN)
    new_login = input(language['new_login'])
    if new_login:
        if checkLoginExists(new_login):
            println_colored(language['login_taken'], Color.RED)
        else:
            user['login'] = new_login
            println_colored(f"{language['login_updated_to']}: {user['login']}", Color.GREEN)

    # New Password
    println_colored(language['edit_password_prompt'], Color.GREEN)
    new_password = input(language['new_password'])
    if new_password:
        confirm_password = input(language['confirm_password'])
        if new_password == confirm_password:
            user['password'] = new_password
            println_colored(f"{language['password_updated']}", Color.GREEN)
        else:
            println_colored(language['password_mismatch'], Color.RED)

    println_colored(f"{language['profile_updated']}", Color.GREEN)


def myProfile(user_id):
    display_loading_animation(language['loading'], Color.MAGENTA)
    user = getUserById(user_id)
    if user:
        println_colored(f"========================== {language['my_profile']} ==========================", Color.CYAN)
        println_colored(
            f"{language['name']}: {user['name']} | {language['login']}: {user['login']} | {language['password']} : {user['password']} | {language['balance']}: {user['balance']}",
            Color.DARK_ORANGE)
        println_colored("============================================================", Color.CYAN)
    else:
        println_colored(f"{language['no_users_found']}", Color.RED)


def myProducts(user_id):
    display_loading_animation(language['loading'], Color.MAGENTA)
    user = getUserById(user_id)
    if user:
        myProducts = user.get("myProducts", [])
        println_colored(f"========================== {language['my_products']} ==========================", Color.CYAN)
        for product in myProducts:
            println_colored(
                f"ID: {product['id']} | {language['name']}: {product['product_name']} | {language['price']}: {product['product_price']} | {language['date']}: {product['product_date']}",
                Color.DARK_ORANGE)
        println_colored("============================================================", Color.CYAN)
    else:
        println_colored(f"{language['no_users_found']}", Color.RED)


def sortExpensiveProduct():
    display_loading_animation(language['loading'], Color.MAGENTA)
    println_colored(f"========================== {language['expensive_product_list']} ==========================",
                    Color.YELLOW)
    filtered_products = sorted(products, key=lambda product: product['product_price'], reverse=True)
    for product in filtered_products:
        println_colored(
            f"ID: {product['id']} | {language['name']}: {product['product_name']} | {language['price']}: {product['product_price']} | {language['date']}: {product['product_date']}",
            Color.DARK_ORANGE)
    println_colored("============================================================", Color.YELLOW)


def buyProduct(user_id):
    display_loading_animation(language['loading'], Color.MAGENTA)
    user = getUserById(user_id=user_id)

    if not user:
        println_colored(language['user_not_found'], Color.RED)
        return

    println_colored(language['product_list'], Color.BLUE)
    for product in products:
        if product not in user["myProducts"]:
            println_colored(
                f"ID: {product['id']} -> {product['product_name']} | {language['price']}: {product['product_price']}",
                Color.GREEN)

    product_id = input(language['choice_product'])
    product = getProductById(product_id)

    if not product:
        println_colored(language['invalid_product'], Color.RED)
        return

    if user["balance"] < int(product["product_price"]):
        println_colored(language['insufficient_balance'], Color.RED)
        return

    user["balance"] -= int(product["product_price"])
    println_colored(f"{language['success_bought_product']} {language['remaining_balance']} {user['balance']}", Color.GREEN)

    user["myProducts"].append(product)

    product["sold_count"] += 1


def productList(user_id):
    display_loading_animation(language['loading'], Color.MAGENTA)
    while True:
        if not products:
            println_colored(language['no_products'], Color.RED)
        else:
            println_colored(f"========================== {language['products']} ==========================", Color.CYAN)
            for product in products:
                println_colored(
                    f"ID: {product['id']} {language['name']}: {product['product_name']} | {language['price']}: {product['product_price']} | {language['date']}: {product['product_date']}",
                    Color.DARK_ORANGE)

            println_colored("============================================================", Color.CYAN)
            print(f"\n1. {language['add_to_favorites']}")
            print(f"2. {language['product_details']}")
            print(f"3. {language['back']}")

            action = input(language["choice"])

            if action == "1":
                product_id = int(input(language["enter_product_id"]))
                addToFavorites(user_id, product_id)
            elif action == '2':
                product_id = int(input(language["enter_product_id"]))
                productDetail(product_id=product_id, user_id=user_id)
            elif action == "3":
                return
            else:
                println_colored(language["invalid_choice"], Color.RED)


def productDetail(product_id, user_id):
    display_loading_animation(f'{language["loading"]}', Color.YELLOW)
    while True:
        product = getProductById(product_id=product_id)

        if not product:
            print(f"{language['product_not_found']}!")
            return

        println_colored(f"\n==== {language['product_detail']} ====", Color.DARK_ORANGE)
        print(f"{language['name']}: {product['product_name']}")
        print(f"{language['price']}: {product['product_price']}")
        print(f"{language['date']}: {product['product_date']}")

        println_colored(f"\n{language['comments']}:", Color.YELLOW)
        if len(product["comments"]) == 0:  # Correctly check if there are no comments
            println_colored(f"{language['no_comments']}", Color.MAGENTA)
        else:
            for idx, comment in enumerate(product["comments"], start=1):
                print(f"{idx}. {comment['login']} ({comment['date']}): {comment['text']}")

        print(f"\n1. {language['add_comment']}")
        print(f"2. {language['remove_comment']}")
        print(f"3. {language['back']}")

        action = input(f"{language['choice']} ")
        if action == "1":
            addComment(user_id, product_id)
        elif action == "2":
            comment_index = input(f"{language['input_comment_id']}: ")
            if comment_index.isdigit():
                removeComment(product_id, int(comment_index) - 1, user_id)
            else:
                println_colored(f"{language['invalid_index']}", Color.RED)
        elif action == "3":
            return
        else:
            println_colored(f"{language['invalid_choice']}", Color.RED)


def addComment(user_id, product_id):
    product = getProductById(product_id)

    if not product:
        println_colored(f"{language['product_not_found']}!", Color.RED)
        return

    user = getUserById(user_id=user_id)

    if not user:
        println_colored(f"{language['user_not_found']}!", Color.RED)
        return

    comment_text = input(f"{language['input_comment']} ").strip()
    if not comment_text:
        println_colored(f"{language['comment_empty']}", Color.RED)
        return

    # Add the comment
    comment = {
        "login": user["login"],
        "date": get_current_date(),
        "text": comment_text
    }
    product["comments"].append(comment)
    println_colored(f"{language['comment_added_successfully']}", Color.GREEN)


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def removeComment(product_id, comment_index, user_id):
    product = getProductById(product_id)

    if not product:
        println_colored(f"{language['product_not_found']}!", Color.RED)
        return

    if comment_index < 0 or comment_index >= len(product["comments"]):
        println_colored(f"{language['invalid_index']}", Color.RED)
        return

    user = getUserById(user_id)

    if not user:
        println_colored(f"{language['user_not_found']}!", Color.RED)
        return

    # userni commenti ekanligiga tekshirish
    comment = product["comments"][comment_index]
    if comment["login"] != user["login"]:
        println_colored(f"{language['cannot_delete_others_comment']}", Color.RED)
        return

    removed_comment = product["comments"].pop(comment_index)
    println_colored(f"{language['comment_removed']}: {removed_comment['text']}", Color.GREEN)


def addToFavorites(user_id, product_id):
    user = getUserById(user_id)

    product = getProductById(product_id)

    if not user:
        println_colored(f"{language['user_not_found']}", Color.RED)
        return
    if not product:
        println_colored(f"{language['product_not_found']}", Color.RED)
        return

    if product in user["favoriteProducts"]:
        println_colored(f"{language['already_favorites']}.", Color.RED)
        return

    user["favoriteProducts"].append(product)
    println_colored(f"{language['add_to_favorites']}", Color.DARK_ORANGE)


def myBalance(user_id):
    display_loading_animation(language['loading'], Color.MAGENTA)
    user = getUserById(user_id)
    if user:
        balance = user["balance"]
        println_colored(f"{language['your_current_balance']}: {balance}", Color.GREEN)
    else:
        println_colored(f"{language['no_users_found']}", Color.RED)


def addBalance(user_id):
    user = getUserById(user_id)
    display_loading_animation(f"{language['loading']}",Color.YELLOW)
    if user:
        amount=int(input(f"{language['enter_amout']}"))
        if amount>0:
            user['balance'] = user['balance'] + amount
        else:
            println_colored(f"{language['invalid_amount']}",Color.CYAN)
    else:
        println_colored(f"{language['no_users_found']}",Color.RED)

def userPage(user_id,lang):
    global language
    language=lang
    user = getUserById(user_id)
    println_colored(f"{language['welcome']} {user['name']}!", Color.GREEN)
    while True:
        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {language['product_list']}", Color.CYAN)
        println_colored(f"2 -> {language['my_balance']}", Color.CYAN)
        println_colored(f"3 -> {language['add_balance']}", Color.CYAN)  # Balans qo'shish
        println_colored(f"4 -> {language['buy_product']}", Color.CYAN)
        println_colored(f"5 -> {language['expensive_product_list']}", Color.CYAN)
        println_colored(f"6 -> {language['my_products']}", Color.CYAN)
        println_colored(f"7 -> {language['my_profile']}", Color.CYAN)
        println_colored(f"8 -> {language['edit_profile']}", Color.CYAN)
        println_colored(f"9 -> {language['search_product']}", Color.CYAN)
        println_colored(f"10 -> {language['favorite_product']}", Color.CYAN)
        println_colored(f"11 -> {language['delete_account']}", Color.CYAN)
        println_colored(f"12 -> {language['contact_admin']}", Color.CYAN)
        println_colored(f"13 -> {language['exit_account']}", Color.CYAN)
        println_colored("==================================", Color.DARK_ORANGE)

        choose = input(language['choice'])

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
            searchProduct(user_id)
        elif choose == '10':
            favoriteProduct(user_id)
        elif choose == '11':
            confirm = input(f"{language['confirm_removal_account']} (y/n): ").strip().lower()
            if confirm == 'y':
                display_loading_animation(language['loading'], Color.CYAN)
                if delete_account(user_id):
                    println_colored(f"{language['account_deleted']}", Color.GREEN)
                    return
            else:
                println_colored(language['removal_cancelled'], Color.RED)
        elif choose == '12':
            contact_admin(user_id)
        elif choose == '13':
            confirm = input(f"{language['confirm_logout']} (y/n): ").strip().lower()
            if confirm == 'y':
                display_loading_animation(language['loading'], Color.CYAN)
                println_colored(f"{language['account_exited']}", Color.GREEN)
                return
            else:
                println_colored(language['action_cancelled'], Color.RED)
        else:
            println_colored(language['invalid_choice'], Color.RED)
