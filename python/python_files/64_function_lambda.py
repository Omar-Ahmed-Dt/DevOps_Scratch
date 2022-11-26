# -------------------------------------------------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

def seperator_():
    print("#" * 50)


def say_hello(name):
    return f"Hello {name}"


print(say_hello("Omar"))
print(say_hello.__name__)       # Print The name of function: say_hello

seperator_()

# Lambda Function  : You Must Stop Format Of Code in Vcode # # #
# Not Write Name For Lambda Function && Not Write (return) :
# hello = lambda name : f"Hello {name}"
# hello is not name of function, it is the variable that contain the value of the function

# print(hello("Omar"))
# print(hello.__name__)         # Print: <lambda>
# print(type(hello))            # Print: <class 'function'>

seperator_()

# hello = lambda name,age : f"Hello {name}, Your Age Is {age}"
# print(hello("Omar",24))
