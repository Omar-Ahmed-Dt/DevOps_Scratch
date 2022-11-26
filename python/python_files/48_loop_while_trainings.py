# -------------------------------------
# --------- Loop => While -------------
# While Condition Is True -------------
# ------ Code Will Run-----------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF))

a = 0
while a < len(myF):
    print(f"#{str(a+1).zfill(2)}: {myF[a]}")
    a += 1
else:
    print("all friends printed to screen..")

# or

# a = 9
# b = 1
# while a >= 0:
#     print(f"#{str(b).zfill(2)}: {myF[a]}")
#     b += 1
#     a -= 1
# else:
#     print("all friends printed to screen..")
