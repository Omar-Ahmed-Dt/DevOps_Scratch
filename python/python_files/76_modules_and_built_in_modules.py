# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import random

# Import One Or Two Functions From Module
# from random import randint
from random import randint, randrange

# Import All Function From The Module
# from random import *

# print(random)
print(f"Print Random Float Number {random.random()}")

print("#"*50)

# Show All Functions Inside Module
print(dir(random))

print("#"*50)

# Import One Or Two Functions From Module
print(f"Print Random int {randint(10,20)}")

print("#"*50)

print(f"{randrange(1,100)}")
