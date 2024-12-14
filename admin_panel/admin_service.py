from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz,lang
from admin_panel.admin_data import checkUserAdmin, admin_info
from user_panel.user_data import users, checkUser, getUserId
from user_panel.user_service import userPage

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

def admin_page():
    while True:
        println_colored("==================================", Color.DARK_ORANGE)
        println_colored(f"1 -> {lang['add_product']}", Color.GREEN)
        println_colored(f"2 -> {lang['edit_product']}", Color.CYAN)
        println_colored(f"3 -> {lang['most_sold_product']}", Color.MAGENTA)
        println_colored(f"4 -> {lang['my_shop_balance']}", Color.MAGENTA)
        println_colored(f"5 -> {lang['search_product']}", Color.MAGENTA)
        println_colored(f"6 -> {lang['all_product_price']}", Color.MAGENTA)
        println_colored(f"7 -> {lang['message_with_user']}", Color.MAGENTA)
        println_colored(f"8 -> {lang['user_list']}", Color.MAGENTA)
        println_colored(f"9 -> {lang['most_buyer_user']}", Color.MAGENTA)
        println_colored(f"10 -> {lang['remove_product']}", Color.MAGENTA)
        println_colored(f"11 -> {lang['log_out']}", Color.MAGENTA)
        choose = int(input(lang['choice']))