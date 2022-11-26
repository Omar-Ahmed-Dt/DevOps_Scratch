# ----------------------------------------------
# ------ Data And Time => Introduction ---------
# ----------------------------------------------

from omar import seperator_ as sep
import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print Current Date and Time
print(datetime.datetime.now())

sep(50)

# Print Current Year
print(datetime.datetime.now().year)

sep(50)
# Print Current Month
print(datetime.datetime.now().month)

sep(50)
# Print Current Day
print(datetime.datetime.now().day)

sep(50)
# Print Start and End of Date
print(datetime.datetime.min)
print(datetime.datetime.max)

sep(50)
# Print Current Time Only
print(datetime.datetime.now().time())

sep(50)
# Print Current Time Type
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

sep(50)
# Print Specific Date
print(datetime.datetime(1998, 2, 9))
print(datetime.datetime(1998, 2, 9, 10, 30, 3, 200))

sep(50)
mybirth_day = datetime.datetime(1998, 2, 9)
date_now = datetime.datetime.now()
print(f"My Birth Day is {mybirth_day} And ", end="")
print(f"Date Now is {date_now}")
sep(50)
print(f"I Lived For {date_now - mybirth_day}")
print(f"I Lived For {(date_now - mybirth_day).days} days.")
