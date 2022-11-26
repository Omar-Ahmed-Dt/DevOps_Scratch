# -----------------------------------------------------------------------
# --- Pylint => For Better Code -----------------------------------------
# -----------------------------------------------------------------------
# ---------------- Terminal => python -m pylint filepath.py -------------

"""
This is My Module
To Say Hello 
"""


def say_hello(name):
    '''' This Function To Say Hello For Users'''
    msg = "Hello"
    return f"{msg} {name}"


print(say_hello("Omar"))
