from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz,current_language
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
        println_colored("1 -> Add Product")
        println_colored("2 -> Edit Product")
        println_colored("3 -> Most Sold Product")
        println_colored("3 -> My Shop Balance")
        println_colored("4 -> Search Product")
        println_colored("5 -> All Product Price")
        println_colored("6 -> Message with User")
        println_colored("7 -> User List")
        println_colored("8 -> Ban User !")
        println_colored("9 -> log out")