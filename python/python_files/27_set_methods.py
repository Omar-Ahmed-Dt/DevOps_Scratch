# ----------------------
# ---------Set Methods--
# ----------------------

# [1] clear()
a = {1, 2, 3}
a.clear()
print(a)

# [2] union()
b = {"A", "c", "b"}
c = {1, 2, 3}
print(b | c)
print(b.union(c))

b = {"A", "c"}
c = {1, 2}
t = {"Omar"}
print(b | c | t)
print(b.union(c, t))

# [3] add()
d = {1, 2, 3}
d.add(4)
d.add(5)
# d.add(4, 5)     # Error: takes one argument
print(d)

# [4] copy() => Shallow Copy
e = {1, 2, 3}
f = e.copy()
print(f)

e.add(6)
print(e)
print(f)    # shallow copy  not deep copy

# [5] remove()
g = {1, 2, 3, 4}
g.remove(2)
print(g)

# g.remove(7)
# print(g)      # Error , 7 not found

# [6] discard()
g = {1, 2, 3, 4}
g.discard(2)
print(g)

g.discard(7)
print(g)    # if element not found , not give Error

# [7] pop() => return random element
p = {"Omar", "Ahmed", "Mohamed"}
print(p.pop())

# [8] update()
j = {"Omar", "Ahmed", "Mohamed"}
o = {1, 2, 3, 4, "Omar"}
j.update(o)
print(j)    # update and remove duplicate values

j = {"Omar", "Ahmed", "Mohamed"}
l = ["Toqa", "Ali"]
o = {1, 2, 3, 4, "Omar"}
j.update(l)     # update by list
j.update(o)
print(j)
