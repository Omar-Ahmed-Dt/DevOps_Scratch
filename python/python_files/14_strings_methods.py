# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()
# To convert each word of the sentence to the list
a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))     # - : it is the seperator

c = "I-Love-Python-and-PHP-and-MySQL"
# 2 : maxsplit and since then put another words in one list
print(c.split("-", 2))
# print(c.split("-", 5))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))

# center()

e = "omar"
# by default whitespace  if i not give argument to function
print(e.center(10))  # 9 => total characters
print(e.center(10, "#"))  # Hashes
print(e.center(16, "@"))  # @
print(e.center(16, "*"))  # *

# count()
f = "I Love Python and PHP Because PHP is Easy"
# في الجملة PHPبيشوف عدد مرات كلمة
print(f.count("PHP"))  # 2 PHP Words
# start index and end index => 0, 25
# only one PHP between index 0 and 25
print(f.count("PHP", 0, 25))

# swapcase()
# swap sensitive case
g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "I Love Python"
# check if the sentence start with [I] if yes return True ,if no retun False
print(i.startswith("I"))    # return True
print(i.startswith("S"))    # return False
print(i.startswith("P", 7, 12))

# endswith()

j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))
