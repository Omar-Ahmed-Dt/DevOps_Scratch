# -------------------------
# ----- Loop => For -------
# -------------------------

# [1] rang()
mynum = range(1, 100)
for num in mynum:
    print(num)

print("#" * 50)

# [2] dictionary()
mydic = {"httml": "80%", "Css": "50%", "Python": "90%"}
# print(mydic["httml"])          # Print: 80%
# print(mydic.get("httml"))      # Print: 80%

for d in mydic:
    # print(mydic[d])         # Print: 80%
    # print(d)                # Print: httml
    print(f"My Progress in Lang {d} is: {mydic[d]}")
