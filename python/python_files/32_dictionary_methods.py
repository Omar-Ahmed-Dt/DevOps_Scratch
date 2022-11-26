# ---------------------------------
# --------Dictionary Methods-------
# ---------------------------------

# [1] setdefault()
user = {
    "name": "Omar",
    "age": 23
}

print(user)
# the name (key) is found , so will no update  the code by name is ahmed :
user.setdefault("name", "Ahmed")
print(user)

print("=" * 50)

user2 = {
    "age": 23
}

print(user2)
# the name (key) is not found , so will update  the code by name is ahmed :
print(user2.setdefault("name", "Ali"))
print(user2)

print("=" * 50)

# [2] popitem()
mydict = {
    "name": "Omar"
}
mydict.update({"age": 24})
print(mydict.popitem())     # Print the last updated

print("=" * 50)

# [3] items()
view = {
    "name": "Omar"
}
all = view.items()
print(view)
view["age"] = 24
print(all)

print("=" * 50)

# [4] fromkeys()
a = {"key1", "key2", "key3"}    # keys
b = "X"         # values
print(dict.fromkeys(a, b))
