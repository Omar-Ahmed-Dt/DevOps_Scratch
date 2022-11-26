# --------------------------------------------------
# --------- Packing And Unpacking Arguments *Args --
# --------------------------------------------------
def seperator_():
    print("#" * 50)


mylist = [1, 2, 3, 4, 5]
print(mylist)
print(*mylist)      # * => asterisk

seperator_()

# [1] First Method


def say_hello(n1, n2, n3):
    people = [n1, n2, n3]
    for name in people:
        print(f"Hello {name}")


# Must Enter 3 Arguments (Limited to 3 Arguments) :
say_hello("Omar", "Mohame", "Ali")

seperator_()

# [2] Second Method


def say_hello(*people):
    for name in people:
        print(f"Hello {name}")


# Not limited to a certain number of Argumets :
say_hello("Omar", "Mohame", "Ali", "Ahmed", "Osama")


seperator_()


def def_skills(*skills):
    for i in skills:
        print(i)


def_skills("Python", "Ccnp", "Cloud")


seperator_()


def def_skills(name, *skills):
    print(f"Hello {name.capitalize()} Your Skills is: ")
    for i in skills:
        print(i)


def_skills("omar", "Python", "Ccnp", "Cloud")
