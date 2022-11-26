# --------------------------
# type() =>> built-in-function to show type of data
# All data in python is object
# ---------------------------

print(type(10))     # int =>> Integer
print(type(-40))    # int =>> Integer

print(type(30.93))  # float =>> Floating point number
print(type(-2.67))  # float =>> Floating point number

print(type("Hello Python"))     # str =>> String

print(type([1, 2, 3, 4, 5]))    # list =>> List , [] : Square brackets

print(type((1, 2, 3, 4, 5)))    # tuple =>> Tuple , () : Parenthesis

print(type({"Omar": 1, "Ahmed": 2, "Mohamed": 3}))     # dict =>> Dictionary

print(2 == 2)
print(2 == 4)
print(type(2 == 2))     # bool =>> Boolean
print(type(2 == 4))     # bool =>> Boolean
