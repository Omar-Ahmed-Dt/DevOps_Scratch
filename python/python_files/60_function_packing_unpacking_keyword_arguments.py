# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------
def seperator_():
    print("#" * 50)


def show_skills(*skills):       # * : Used When You not know number of arguments
    # print(type(skills))         # Print: <class 'tuple'>
    for i in skills:
        print(i)


show_skills("Python", "Network", "Virtualization")

seperator_()


def show_skills(**skills):
    # print(type(skills))         # Print: <class 'dict'>
    for i, y in skills.items():
        print(f"{i.capitalize()} => {y}")


show_skills(Python="90%", Network="50%")

seperator_()

mydict = {
    "Python": "90%",
    "Network": "50%",
    "Go": "40%"
}


def show_myskills(skills):
    for i, y in skills.items():
        print(f"{i.capitalize()} => {y}")


show_skills(**mydict)
