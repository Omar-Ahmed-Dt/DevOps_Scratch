# ----------------------
# ---------Set Methods--
# ----------------------

# [1] difference()
a = {1, 2, "Omar", "Ahmed"}
b = {1, 2, 3, 4}
print(a)
print(a.difference(b))      # Print: {'Ahmed', 'Omar'} => a - b
print(a - b)
print(b.difference(a))      # Print: {3, 4}  => b - a
print(b-a)

print("=" * 40)     # Seperator

# [2] difference_update()
p = {1, 2, 3, 4}
c = {1, 2, "Omar", "Ahmed"}
print(p)
p.difference_update(c)
print(p)        # Print: {3, 4}

print("=" * 40)     # Seperator

# [3] intersection()
e = {1, 2, 3, 4, "X"}
f = {"Omar", "X", 2}
print(e)
print(e.intersection(f))    # Print: {2, 'X'} => e & f

print("=" * 40)     # Seperator

# [4] intersection_update()
e = {1, 2, 3, 4, "X"}
f = {"Omar", "X", 2}
e.intersection_update(f)
print(e)        # Print: {2,'X'}

print("=" * 40)     # Seperator

# [5] symmetric_difference()
g = {1, 2, 3, 4, "X"}
l = {"Omar", "X", 2}
print(g.symmetric_difference(l))        # Print: {1, 3, 4, 'Omar'} => g ^ l

print("=" * 40)     # Seperator

# [6] symmetric_difference_update()
i = {1, 2, 3, 4, "X"}
o = {"Omar", "X", 2}
i.symmetric_difference_update(o)
print(i)

print("=" * 40)     # Seperator
