# -----------------------------
# -- Set ----------------------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# [1] Not Ordered
myset = {"Omar", "Ahmed", 100}
# Print : {'Ahmed', 100, 'Omar'} || {'Omar', 100, 'Ahmed'} || {'Ahmed', 'Omar', 100} => Not Ordered
print(myset)

# [2] Not Indexed
a = {1, 2, 3, 4, 5}
# print(a[1])

# [3] Can't Slicing
a = {1, 2, 3, 4, 5}
# print(a[1:3])

# [4] Has Only Immutable Data like Tuple not List and not Dict
# b = {"Omar", True, 2, 4, 3.04, [6, 7, 8]}
# print(b)    # Error:  unhashable type: 'list' => list not immutable data

b = {"Omar", True, 2, 4, 3.04, (6, 7, 8)}
print(b)

# [5] Items Is Unique
c = {1, 2, 3, 3, "Omar", "Ahmed", "Omar"}
print(c)
