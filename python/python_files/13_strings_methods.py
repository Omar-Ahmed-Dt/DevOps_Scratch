# --------------------------
# ---------Strings Methods--
# --------------------------

a = "I love Python"
b = "      I love Python     "
print(len(a))
print(len(b))

# [1] strip() rstrip() lstrip()
# To remove whitespace
print(b.strip())    # remove left and right whitespace
print(b.rstrip())   # remove right whitespace
print(b.lstrip())   # remove left whitespace
print(len(b.lstrip()))

# To remove any character
b = "#####I love Python#####"
print(b.strip("#"))
print(b.rstrip("#"))
print(b.lstrip("#"))

b = "@#@#@I love Python#@#@#"
print(b.strip("@#"))
print(b.rstrip("@#"))
print(b.lstrip("@#"))

# [2] title()
# To convert first char of any word and a char after number to capital letter
varr = "i love 2d graphics and 3g technology and python"
print(varr.title())

# [3] capitalize()
# To convert first char of sentence to capital letter
capp = "i love 2d graphics 3g technology and python"
print(capp.capitalize())

# [4] zfill()  => zero fill
a, b, c = "3", "11", "2"
print(a)
print(b)
print(c)

print(a.zfill(2))   # 2 => xx pattern of the biggest number
print(b.zfill(2))
print(c.zfill(2))

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))  # 4 => xxxx pattern of the biggest number
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# [5] upper()
g = "omar"
print(g.upper())

# [6] lower()
g = "OMAR"
print(g.lower())
