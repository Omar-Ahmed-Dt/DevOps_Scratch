# ------------------------------------------------------
# ------------ Function Scope --------------------------
# ------------------------------------------------------

def seperator_():
    print("#" * 50)


x = 1       # Global Scope


def one():
    print(x)


print(x)    # Print: 1
one()       # Print: 1

seperator_()

y = 1


def one():
    y = 2
    print(y)


print(y)    # Print: 1
one()       # Print: 2

seperator_()


def one():
    z = 2
    print(z)


# print(z)    # Print: 'z' is not defined | z is not have Global Value
one()       # Print: 2


seperator_()


def one():
    global r    # r is Global now
    r = 2
    print(r)


one()       # Print: 2
print(r)    # Print: 2


def two():
    print(r)


two()       # Print: 2
