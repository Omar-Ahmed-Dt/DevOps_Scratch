# ------------------------------------------
# -- Modules => Install External Packages --
# ------------------------------------------
# [1] Module vs Package
# [2] External Packages Downloaded From The Internet
# [3] You Can Install Packages With Python Package Manager PIP
# [4] PIP Install the Package and Its Dependencies
# [5] Modules List "https://docs.python.org/3/py-modindex.html"
# [6] Packages and Modules Directory "https://pypi.org/"
# [7] PIP Manual "https://pip.pypa.io/en/stable/reference/pip_install/"
# ---------------------------------------------------------------------

# My Test
from omar import format_name as f_n

# In Terminal =>  pip install pyfiglet termcolor
import pyfiglet
import termcolor

# Pyfiglet
# print(dir(pyfiglet))
# print(pyfiglet.figlet_format("Omar Ahemd"))

# Termcolor
# print(termcolor.colored("Omar", color="yellow"))
print(termcolor.colored(pyfiglet.figlet_format("Omar Ahmed"), color="red"))
print(termcolor.colored(pyfiglet.figlet_format("#"*3), color="green"))

# Test
f_n("Toqa", "yellow")
