# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Examples (String, List, Set, Tuple, Dictionary)
# ------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using iter() Method
# [3] For Loop Already Calls iter() Method on The Iterable Behind The Scene
# [4] Gives "StopIteration" If Theres No Next Element
# -----------------------------------------------------------

from omar import seperator_ as sep

# String is Iterable
my_name = "Omar Ahemd"
for n in my_name:
    print(n)
    # print(n, end="")

sep(50)
# List, Set , Tuple and Dictionary are Iterable
name = ["Omar", "Ali"]
for i in name:
    print(i)
sep(50)
numbers = (1, 2, 3, 4,)
for num in numbers:
    print(num)

sep(50)
# Numbers are Not Iterable
# nums = 100
# for nn in nums:
#     print(nn)     # Print: TypeError: 'int' object is not iterable

# sep(50)
# Generate Iterator From Iterable Using iter() Method
myinterator = iter(my_name)
print(next(myinterator))
print(next(myinterator))
print(next(myinterator))
print(next(myinterator))
print(next(myinterator))
print(next(myinterator))
print(next(myinterator))
print(next(myinterator))
print(next(myinterator))
print(next(myinterator))

sep(50)

# Loop Using iter() Bydefault
for letter in "Python":
    print(letter)

for let in iter("Python"):
    print(let)
