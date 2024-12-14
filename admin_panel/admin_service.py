from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz, lang
from admin_panel.admin_data import checkUserAdmin, admin_info
from user_panel.user_data import users, checkUser, getUserId
from user_panel.user_service import userPage
from datetime import datetime

products = []


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
    display_loading_animation(lang['loading'],Color.CYAN) # Dizayn uchun
    println_colored(lang['success_added_product'], Color.GREEN)



def editProduct():
    pass


def admin_page():
    while True:
        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {lang['add_product']}", Color.MAGENTA)
        println_colored(f"2 -> {lang['edit_product']}", Color.MAGENTA)
        println_colored(f"3 -> {lang['most_sold_product']}", Color.MAGENTA)
        println_colored(f"4 -> {lang['my_shop_balance']}", Color.MAGENTA)
        println_colored(f"5 -> {lang['search_product']}", Color.MAGENTA)
        println_colored(f"6 -> {lang['all_product_price']}", Color.MAGENTA)
        println_colored(f"7 -> {lang['message_with_user']}", Color.MAGENTA)
        println_colored(f"8 -> {lang['user_list']}", Color.MAGENTA)
        println_colored(f"9 -> {lang['most_buyer_user']}", Color.MAGENTA)
        println_colored(f"10 -> {lang['remove_product']}", Color.MAGENTA)
        println_colored(f"11 -> {lang['log_out']}", Color.MAGENTA)
        println_colored("==================================", Color.DARK_ORANGE)
        choose = int(input(lang['choice']))
        if choose == 1:
            addProduct()
        elif choose == 2:
            editProduct()
        elif choose == 3:
            pass
        elif choose == 4:
            pass
        elif choose == 5:
            pass
        elif choose == 6:
            pass
        elif choose == 7:
            pass
        elif choose == 8:
            pass
        elif choose == 9:
            pass
        elif choose == 10:
            pass
        elif choose == 1:
            pass
        else:
            println_colored(lang["invalid_choice"], Color.RED)
