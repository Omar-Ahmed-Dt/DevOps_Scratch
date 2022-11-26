# ---------------------------------------------------------
# --- Decorators => Practical Speed Test ------------------
# ---------------------------------------------------------

from omar import seperator__ as sp
from time import time

# Decorator With Parameters
# def mydecorator(func):
#     def nestedfunction(*numbers):
#         for number in numbers:
#             # if numbers[0] < 0 or numbers[1] < 0:
#             if number < 0:
#                 print("One of The Num is Less Than Zero")
#         func(*numbers)

#     return nestedfunction


# @mydecorator
# def calculate(n1, n2, n3, n4):
#     print(n1+n2+n3+n4)


# calculate(10, 90, 80, -4)

# sp()

def speedtest(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Function Running Time is: {end - start}")
    return wrapper


@speedtest
def bigloop():
    for i in range(1, 2000):
        print(i)


bigloop()
