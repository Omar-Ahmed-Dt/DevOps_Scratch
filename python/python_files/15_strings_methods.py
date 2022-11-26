# ------------------------
# --------Strings Methods-
# ------------------------

# [1] index(substring,start,end)
a = "I love Python People"
print(a.index("P"))
print(a.index("P", 0, 8))
# If not found will return : ValueError :
# print(a.index("p"))

# [2] find(substring,start,end)
a = "I love Python"
print(a.find("P"))
print(a.find("P", 0, 8))
# If not found will return : -1 :
# print(a.find("p"))

# [3] rjust(width,fill char) && ljust(width,fill char)
name = "ali"
print(name.rjust(10))
print(name.rjust(10, "*"))
print(name.ljust(10, "!"))

# [4] splitlines()
name = '''omar 
ahmed 
"ohamed'''
name2 = "omar\nahmed\nmohamed"
print(name.splitlines())
print(name2.splitlines())

# [5] expandtabs() => to control of tabs between words
name = "omar\tahmed\tmohamed\talshishiny"   # \t : To make tabs between words
print(name)
print(name.expandtabs(30))

# [6] istitle() => return True or False
name = "I Love Python And 3G"
name2 = "I love python And 3g"
print(name.istitle())
print(name2.istitle())

# [7] isspace()
a = " "
b = ""
print(a.isspace())
print(b.isspace())

# [8] islower() && isupper()
v = "i love python"
vt = "I love python"
vu = "I LOVE PYTHON"
vuu = "I love python"
print(v.islower())
print(vt.islower())
print(vu.isupper())
print(vuu.isupper())

# [9] isidentifier()
# To check a string is valid or not
i = "omar ahmed"
ii = "omar_ahmed"
iii = "omar--ahmed"
iiii = "omarahmed"
print(i.isidentifier())
print(ii.isidentifier())
print(iii.isidentifier())
print(iiii.isidentifier())

# [10] isalpha()
b = "omarahmed"
bb = "omar_ahmed"
bbb = "omar53"
print(b.isalpha())
print(bb.isalpha())
print(bbb.isalpha())

# [11] isalnum() => To check that string is alpha && number
bb = "omar ahmed"
bbb = "omar53"
print(bb.isalnum())
print(bbb.isalnum())
