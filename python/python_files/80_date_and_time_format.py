# --------------------------------------------
# ----- Date and Time Formats ----------------
# ---  https://strftime.org/ -----------------
# --------------------------------------------

from omar import seperator_ as sp
import datetime

mybirthday = datetime.datetime(1998, 2, 9)
# print(dir(datetime.datetime))
print(mybirthday)
print(mybirthday.strftime("%B"))    # Print: February
print(mybirthday.strftime("%b"))    # Print: Feb
print(mybirthday.strftime("%A"))    # Print: Monday
print(mybirthday.strftime("%a"))    # Print: Mon

sp(50)

print(mybirthday.strftime("%d %B %Y"))  # Print: 09 February 1998

sp(50)

print(mybirthday.strftime("%d,%B,%Y"))

sp(50)

print(mybirthday.strftime("%d/%B/%Y"))
