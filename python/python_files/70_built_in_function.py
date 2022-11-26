# ------------------------
# -- Built In Functions --
# ------------------------
# sum()
# round()
# range()
# print()
# ------------------------

def seperator_():
    print("#" * 50)


# sum(iterable, start)
a = [1, 10, 19, 40]
print(sum(a))       # Print: 70
print(sum(a, 40))   # Print: 70 + 40

seperator_()

# round(number, numofdigits)
print(round(150.501))       # 150.501 ~ 151
print(round(150.554, 2))

seperator_()
# range(start, end, step)
print(list(range(0)))
print(list(range(10)))
print(list(range(0, 20, 2)))

seperator_()
# print()
print("Hello @ Osama @ How @ Are @ You")
print("Hello", "Osama", "How", "Are", "You", sep=" | ")

print("First Line", end=" $$ ")     # Default for end => (Enter) => New Line
print("Second Line")
print("Third Line")
