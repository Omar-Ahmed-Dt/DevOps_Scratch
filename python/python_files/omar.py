# -----------------------------------------------------
# ---- My Module Is Used In 77_modules_creat.py -------
# -----------------------------------------------------

import termcolor
import pyfiglet


def say_hello(name):
    print(f"Hello {name}")


def how_age(name):
    print(f"how are {name}")


def seperator_(sep_):
    print("#"*sep_)


def seperator__():
    print("#"*50)


def format_name(name, user_color):
    print(termcolor.colored(pyfiglet.figlet_format(name), color=user_color))
