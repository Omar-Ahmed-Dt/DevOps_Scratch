# ------------------- Test --------------------------
from time import time
from omar import seperator__ as sp
# ------------------- Map -----------------------------

# def fix_name(name):
#     return name.strip().capitalize()
from functools import reduce


mylist = ["  omar  ", "ahmed  "]

# for i in map(fix_name, mylist):
#     print(i)

#

for i in map(lambda name: name.strip().capitalize(), mylist):
    print(i)

# ------------------- Filter -----------------------------


def fix_name(name):
    return name.startswith("O")


mylist = ["  omar  ", "ahmed  ", "Omar"]
for i in filter(fix_name, mylist):
    print(i)

print("#"*50)

mylistnum = [1, 20, 3, 89]
for i in filter(lambda num: num > 10, mylistnum):
    print(i)

print("#"*50)
# ------------------- Reduce -----------------------------


# def sumall(n1, n2):
#     return n1+n2


mylistnum_ = [1, 20, 3, 89]
# print(reduce(sumall, mylistnum_))
print(reduce(lambda n1, n2: n1 + n2, mylistnum_))

print('#' * 50)

# ------------- Decorator -----------------------------------


def mydecorator(func):
    def nesedfunction():
        print("Before")
        func()
        print("After")
    return nesedfunction


# @mydecorator      # Related With Second Method  ***
def sayhello():
    print("Hello From SayHello Function")


# Call Decorator
# [1] First Mehtod
# mydec = mydecorator(sayhello)
# mydec()

# or

# [2] Second Method   ***
# sayhello()


# ------------- Decorator With Parameters -----------------------------------
def mydecorator_(func):
    def secondfunc(n1, n2):
        func(n1, n2)
    return secondfunc


@mydecorator_
def calc(num1, num2):
    print(num1 + num2)


calc(1, 5)

sp()


def mydecorator_(func):
    def secondfunc(n1, n2):
        if n1 < 0 or n2 < 0:
            print("One of The Nums is Less than Zero")
        func(n1, n2)
    return secondfunc


@mydecorator_
def calc(num1, num2):
    print(num1 + num2)


calc(-9, 5)

sp()

# -------------------------- Decorators With Speed Test ---------------


def mytest(func):
    def nestedfunc():
        starttime = time()
        func()
        endtime = time()
        print(endtime - starttime)
    return nestedfunc


@mytest
def bigloop():
    for i in range(1, 2000):
        print(i)


bigloop()

sp()
