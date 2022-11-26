# -----------------------------------------------------------------
# -- Generators --
# -----------------------------------------------------------------
# [1] Generator is a Function With "yield" Keyword Instead of "return"
# [2] It Support Iteration and Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have one or More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not From Begining
# [5] When Called, Its Not Start Automatically, Its Only Give You The Control
# -----------------------------------------------------------------
from omar import seperator_ as sep


def mygenerator():
    yield 1         # Using "yield" Instead of "return"
    yield 2
    yield 3
    yield 4


# print(mygenerator)      # Print: <function mygenerator at 0x000002138FFA03A0>

mygen = mygenerator()
print(next(mygen))      # Print: 1
print(next(mygen))      # Print: 2
# print(next(mygen))
# print(next(mygen))

sep(50)

for n in mygen:
    print(n)        # Not Start From Begining   => Print: 3 & 4

sep(50)
# or

for i in mygenerator():
    print(i)
