# e-commerce app
# First Page -> Sign in, Sign Up,Language (uz,ru,eng)
# Clean ig we use global func and types,
# User Role : User,Admin

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

# ######################### Admin Page ####################
# Add Product
# Edit Product
# Most Buyer Product
# Search Product
# All Product Price
# Message List // Soon
# User List
# Most buyer user a-z list
# Remove Product
# Ban User !
# log out


import time
import threading


class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    DARK_ORANGE = "\033[38;2;170;85;0m"
    RESET = "\033[0m"


def print_colored(text, color=Color.BLUE):
    print(f"{color}{text}{Color.RESET}", end="")


def println_colored(text, color=Color.BLUE):
    print(f"{color}{text}{Color.RESET}")


def display_loading_animation(message, color):
    loading_chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    counter = 0

    def loading():
        nonlocal counter
        try:
            while not stop_event.is_set():
                print_colored(f"\r{loading_chars[counter % len(loading_chars)]} {message}", color)
                counter += 1
                time.sleep(0.1)  # Adjust the delay as needed
        except KeyboardInterrupt:
            pass

    stop_event = threading.Event()
    loading_thread = threading.Thread(target=loading)
    loading_thread.start()

    # Run the loading animation for a few seconds
    time.sleep(1)  # Adjust the duration as needed
    stop_event.set()
    loading_thread.join()

    # Clear the loading line
    print("\r" + " " * len(message) + "\r")
