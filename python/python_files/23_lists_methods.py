#---------------------------
#--------Lists Methods------
#---------------------------

# [1] clear()
a = [1,2,3,4,5]
a.clear()
print(a)

# [2] copy()
a = [1,2,3,4,5]
b = a.copy()    # a is main list && b is copied list 
print(b)

b.append(8)
print(a)
print(b)

# [3] count()
a = [1,2,3,4,1,2,4,5,1]
print(a.count(1))
print(a.count(5))

# [4] index()
e = ["Omar", "Ahmed","Mohamed"]
print(e.index("Ahmed"))
print(e.index("Mohamed"))
print(e.index("Omar"))

# [5] insert() 
y = [1,2,3,"A","B"]
y.insert(0,"Test")      # Instert Object before Index 
print(y)

u = [1,2,3,"A","B"]
u.insert(-1,"Test")     # Index (-1) is : B 
print(u)

# [6] pop()
y = [1,2,3,"A","B"]
print(y.pop(3))
print(y.pop(-1))
