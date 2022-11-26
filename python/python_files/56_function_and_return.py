# -------------------------
# -- Function And Return --
# -------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY (Don't Repeat Yourself)
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# ----------------------------------------

def function_name():
    print("Hello Python")


function_name()

print("#" * 50)


def function_name_2():
    return "Hello Python"


datafromfunction = function_name_2()
# print(function_name_2())
print(datafromfunction)
