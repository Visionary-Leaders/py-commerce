from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz, lang
from admin_panel.admin_data import checkUserAdmin, admin_info





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

def userPage(id:int):
    while True:

        choose= input(lang['choice'])