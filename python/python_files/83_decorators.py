# ----------------------------------------------------------------------
# -- Decorators => Intro --
# ----------------------------------------------------------------------
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)
# ----------------------------------------------------------------------
from omar import seperator__ as sp

# Decorator Accept Parameter as a Function :


def mydecorator(func):     # Decorator
    def nestedFunc():     # Any Name Its Just For Decoration
        print("Befor")    # Message From Decorator
        func()            # Execute  Function
        print("After")    # Message From Decorator

    return nestedFunc


@mydecorator
def sayhello():
    print("Hello From SayHello Function")


@mydecorator
def sayhowareyou():
    print("Hello From SayHowAreYou Function")


sayhello()

# after_mydec = mydecorator(sayhello)
# after_mydec()

sp()

sayhowareyou()
