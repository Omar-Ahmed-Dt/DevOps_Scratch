# ------------------------
# -- Built In Functions --
# ------------------------
# enumerate()
# help()
# reversed()
# ------------------------

# enumerate(iterable, start=0)

mySkills = ["Html", "Css", "Js", "PHP"]

mySkillsWithCounter = enumerate(mySkills, 10)

print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter:

    print(f"{counter} - {skill}")

print("#" * 50)

# help()

print(help(print))

print("#" * 50)

# reversed(iterable)

myString = "Elzero"

print(reversed(myString))   # Print: <reversed object at 0x0000021AB3A1BE20>

for letter in reversed(myString):

    print(letter)

print("#" * 50)

for s in reversed(mySkills):

    print(s)
