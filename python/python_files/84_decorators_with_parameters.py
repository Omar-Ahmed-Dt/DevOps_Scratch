# -----------------------------------------------------
# ---- Decorators => Function With Parameters ---------
# -----------------------------------------------------

from omar import seperator__ as sp


def mydecorator(func):
    def nestedfunction(num1, num2):
        print("Before")
        func(num1, num2)

    return nestedfunction


@mydecorator
def calculate(n1, n2):
    print(n1+n2)


calculate(10, 90)

sp()


def myDecorator_(func):  # Decorator

    def nestedFunc(num1, num2):  # Any Name Its Just For Decoration

        if num1 < 0 or num2 < 0:

            print("Beware One Of The Numbers Is Less Than Zero")

        func(num1, num2)  # Execute Function

    return nestedFunc  # Return All Data


@myDecorator_
def calculate(n1, n2):
    print(n1+n2)


calculate(-5, 90)   # Print: Beware One Of The Numbers Is Less Than Zero


sp()


# Using Two Decorators For The Same Function


def myDecorator__(func):

    def nestedFunc(num1, num2):
        print("Coming From Decorator Two")
        func(num1, num2)

    return nestedFunc


@myDecorator__
@myDecorator_
def cal(n1, n2):
    print(n1+n2)


cal(-9, 80)
