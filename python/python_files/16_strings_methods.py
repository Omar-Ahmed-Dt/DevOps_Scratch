# ------------------------
# --------Strings Methods-
# -----------------------

# [1] replace(old_value,new_value,count)
a = "Hello one two one three one"
print(a.replace("one", "1"))
print(a.replace("one", "1", 1))
print(a.replace("one", "1", 2))


# [2] join()
mylist = ["omar", "ahmed", "mohamed"]
print(" ".join(mylist))
print("-".join(mylist))
print("*".join(mylist))
print(type("-".join(mylist)))
