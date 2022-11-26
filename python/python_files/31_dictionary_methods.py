# ---------------------------------
# --------Dictionary Methods-------
# ---------------------------------

# [1] clear()
user = {
    "name": "Omar"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# [2] update()
user = {
    "name": "Omar"
}
user["age"] = 24
print(user)

print("=" * 50)

# or :
user.update({"location": "NA", "country": "Egypt"})
print(user)

print("=" * 50)

# [3] copy()
b = user.copy()
print(b)

print("=" * 50)

user.update({"Job": "Computer Engineer"})
print(user)
print(b)

print("=" * 50)

# [4] keys() + values()
print(user.keys())
print(user.values())

print("=" * 50)
