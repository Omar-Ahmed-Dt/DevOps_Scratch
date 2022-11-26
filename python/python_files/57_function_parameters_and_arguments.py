# --------------------------------------------------
# ----- Function Parameters And Arguments ----------
# --------------------------------------------------

def seperator_():
    print("#" * 50)


a, b, c = "Osama", "Ahmed", "Sayed"


def say_hello(n):

    print(f"Hello {n}")


say_hello(a)
say_hello(b)
say_hello(c)

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# n                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Ahmed is The Argument

seperator_()


def addition(n1, n2):
    # print(n1 + n2)
    print(int(n1) + int(n2))


# addition("100", 50)         # Error: can only concatenate str (not "int") to str
addition("100", 500)

seperator_()


def addition_2(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Only Integers Allowed")
    else:
        print(n1 + n2)


addition_2(300, 600)
addition_2("100", 900)      # Print: Only Integers Allowed

seperator_()


def name(fname, sname, lname):
    print(f"{fname.strip().capitalize()} {sname.strip().capitalize():.1s} {lname.strip().capitalize()}")


name("omar", "ahmed", "alshishiny")
