from utils.util import println_colored, Color, display_loading_animation
from data.local_data import eng, uz,current_language
from admin_panel.admin_data import checkUserAdmin, admin_info
from user_panel.user_data import users, checkUser, getUserId
from user_panel.user_service import userPage


def admin_page():
    while True:
        println_colored("==================================", Color.DARK_ORANGE)
