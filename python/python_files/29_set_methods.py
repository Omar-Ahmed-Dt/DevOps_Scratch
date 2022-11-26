# ----------------------
# ---------Set Methods--
# ----------------------

# [1] issuperset()
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print(a.issuperset(b))      # Print: True
c = {1, 2, 3, 4, 5, 6}
print(a.issuperset(c))      # Print : False

print("=" * 40)

# [2] issubset()
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print(b.issubset(a))        # Print : True
print(a.issubset(b))        # Print : False

print("=" * 40)

# [3] isdisjoint()
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}
print(a.isdisjoint(b))

a = {10, 20, 30}
b = {1, 2, 3}
print(a.isdisjoint(b))
