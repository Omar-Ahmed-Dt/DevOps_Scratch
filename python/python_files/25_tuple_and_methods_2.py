# ------------------------
# --------Tuple-----------
# ------------------------

# [1] Tuple With One Element
tuple_1 = ("Omar")
tuple_2 = "Omar"
print(type(tuple_1))    # Print : <class 'str'>
print(type(tuple_2))    # Print : <class 'str'>

tuple_1 = ("Omar",)
tuple_2 = "Omar",
print(type(tuple_1))    # Print : <class 'tuple'>
print(type(tuple_2))    # Print : <class 'tuple'>

# [2] Tuple Concatenation
a = (1, 2, 3, 4)
b = (5, 6)

c = a + b
d = a + ("A", "B", True) + b
print(c)
print(d)

# [3] Tuple, List, String Repeat (*)
myString = "Omar"
myList = [1, 2]
myTuple = ("A", "B")
print(myString * 6)
print(myList * 6)
print(myTuple * 6)

# ------------------------

# Methods => count()
a = (1, 3, 7, 8, 2, 6, 5, 8)
print(a.count(8))

# Methods => index()
b = (1, 3, 7, 8, 2, 6, 5)
# print("The Position of Index Is: " + b.index(7))  # Error
print("The Position of Index Is: {:d}".format(b.index(7)))
print(f"The Position of Index Is: {b.index(7)}")

# Tuple Destruct
a = ("A", "B", 4, "C")
x, y, _, z = a      # _ : ignore

print(x)
print(y)
print(z)
