# ---------------------------------------------------------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------

mynumber = [1, 2, 3, 4, 5, 6,  7, 8, 9]

for num in mynumber:
    if num % 2 == 0:
        print(f"=>The Num {num} is Even")
    else:
        print(f"=>The Num {num} is Odd")
else:
    print("Loop Is Finished")

print("#" * 50)

name = "Omar"
for i in name:
    # print(i)
    print([i.upper()])
else:
    print("Loop Is Finished")
