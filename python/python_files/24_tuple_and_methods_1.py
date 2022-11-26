# ------------------------
# --------Tuple-----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item Like List
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# ------------------------

# [1] Tuple Syntax
first_tuple = ("Omar", "Ahmed")
second_tuple = "Omar", "Ahmed"      # Can Remove The Parentheses
print(first_tuple)
print(second_tuple)
print(type(first_tuple))
print(type(second_tuple))

# [2] Tuple Indexing
mytuple = ("Omar", "Ahmed", "Mohamed")
print(mytuple[1])
print(mytuple[-1])

# [3] Tuple Assign Values
mytest = "Omar", "Ahmed", "Mohamed"
# mytest[1] = "Ali"     # Tuple Immutable
# print(mytest)       # Error: 'tuple' object does not support item assignment

# [4] Tuple Items => Different Data Types
myitems = (1, 2, 3, 1, 2.000443, "Omar", "Toqa")
print(myitems)
