# -----------------------------
# -- Lists---------------------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

mylist = ["one","two",1,2,3,True]
print(mylist)       # Print : Whole List 
print(mylist[1])    # Print : two
print(mylist[-1])   # Print : True
print(mylist[-3])   # Print : 2 
print(mylist[1:])   # Print : ['two', 1, 2, 3, True]
print(mylist[1:4])  # Print : ['two', 1, 2]
print(type(mylist[1:4]))    # Print : <class 'list'>
print(mylist[::1])  # Print : Whole List 
print(mylist[::2])  # Print : ['one', 1, 3]

# Can Mutable (Edit)
mylist[-1] = False
mylist[2] = "One" 
print(mylist)
mylist[0:2] = []
print(mylist)
mylist[1:] =["A","B","C"]
print(mylist)
mylist[0:2] =["R"]
print(mylist)
