# ------------------------
# -- Built In Functions --
# ------------------------
# all()
# any()
# bin()
# id()
# ------------------------

def seperator_():
    print("#" * 50)


x = [1, 2, 3, 4]
if all(x):
    print("All Elements is True")
else:
    print("Theres At Least One Element Is False")

seperator_()

x = [1, 2, 3, 4, []]
if all(x):
    print("All Elements is True")
else:
    print("Theres At Least One Element Is False")

seperator_()
# y = [1, 2, 3, 4, []]
y = [0, []]

if any(y):

    print("There's At Least One Element is True")

else:

    print("Theres No Any True Elements")

seperator_()

print(bin(100))

seperator_()

a = 1
b = 2

print(id(a))
print(id(b))
