# ----------------------
# -----Type Conversion--
# ----------------------

# [1] str() => String
a = 10
print(type(a))
print(type(str(a)))

print("=" * 50)

# [2] tuple()
c = "Omar"
l = [1, 2, 3, 4]   # List
s = {"A", "B", "C"}   # Set
f = {1: "A", 2: "B"}   # Dict
print(tuple(c))
print(tuple(l))
print(tuple(s))
print(tuple(f))

print("=" * 50)

# [3] list()
c = "Omar"
l = (1, 2, 3, 4)   # Tuple
s = {"A", "B", "C"}   # Set
f = {1: "A", 2: "B"}   # Dict
print(list(c))
print(list(l))
print(list(s))
print(list(f))

print("=" * 50)

# [4] set()
c = "Omar"
l = (1, 2, 3, 4)   # Tuple
s = ["A", "B", "C"]   # List
f = {1: "A", 2: "B"}   # Dict
print(set(c))
print(set(l))
print(set(s))
print(set(f))

print("=" * 50)

# [5] dict()
c = "Omar"

l = (1, 2, 3, 4)   # Tuple
ll = ((1, "A"), (2, "B"))       # Format of Tuple to convert to dict

s = ["A", "B", "C"]   # List
ss = [[1, "C"], [2, "D"]]      # Format of list to convert to dict

f = {"A", "B"}   # Set not convert to dict

# print(dict(c))        # Error => String not convert to dict
# print(dict(l))        # Error
print(dict(ll))
# print(dict(s))        # Error
print(dict(ss))
# print(dict(f))        # Error  => Set no convert to dict
