# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------

# Line number : 34
# [1] UnPacking for Tuple : *my_Tuples
# [2] UnPacking for Dictionary : **my_Dictionary


def seperator_():
    print("#" * 50)


myskills = {
    "vir": "80%",
    "dfr": "70%",
    "jus": "90%",
    "tru": "30%",
}

mytuples = ("python", "network")


def show_name(name, *skills, **myskills):
    print(
        f"=>Hello {name.capitalize()}: \n=>Your Skills Without Progress are: ")
    # Loop For Tuple :
    for i in skills:
        print(f" - {i}")
    # Loop For Dictionary :
    for x, y in myskills.items():
        print(f" - {x} => {y}")


# show_name("omar")     # When used * and not give value to function, not cause error
# show_name("omar", "Python", "Network", myskills)
show_name("omar", *mytuples, **myskills)
