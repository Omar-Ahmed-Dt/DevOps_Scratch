# -------------------------------------
# ---- Break, Continue, Pass ----------
# -------------------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# [1] Continue
for num in myNumbers:
    if num == 13:
        continue
    print(num)

print("#" * 50)

# [2]  Break
for num in myNumbers:
    if num == 13:
        break
    print(num)

print("#" * 50)

for num in myNumbers:
    print(num)
    if num == 13:
        break

print("#" * 50)

# [3] Pass
# for num in myNumbers:       # Error

for num in myNumbers:         # Not Error
    pass

print("#" * 50)

for num in myNumbers:
    if num == 13:
        pass
    print(num)
