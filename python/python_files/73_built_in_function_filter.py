# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# ---------------------------------------------------------------

def checkNumber(num):
    # if num > 10:
    #     return num
    return num > 10         # Return True | False

# def checkNumber(num):
#     if num == 0:
#         return True


myNumbers = [0, 0, 1, 19, 10, 20, 100, 5, 0]

myResult = filter(checkNumber, myNumbers)
# print(myResult)     # Print: <filter object at 0x0000022D073B16A0>

for number in myResult:
    print(number)

print("#" * 50)


def check_name(name):
    return name.startswith("O")


mynames = ["Omar", "Ali", "Ahmed", "Osama"]

myReturn_data = filter(check_name, mynames)
for person in myReturn_data:
    print(person)

print("#" * 50)

mynames = ["Omar", "Ali", "Ahmed", "Osama"]

myReturn_data = filter(lambda name: name.startswith("O"), mynames)
for p in myReturn_data:
    print(p)

print("#" * 50)

mynames = ["Omar", "Ali", "Ahmed", "Osama"]

# myReturn_data = filter(lambda name: name.startswith("O"), mynames)
for p in filter(lambda name: name.startswith("O"), mynames):
    print(p)
