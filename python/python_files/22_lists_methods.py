#---------------------------
#--------Lists Methods------
#---------------------------

# [1] Append() => Add Elements to End of List 
myfriends = ["Omar","Ahmed","Mohamed"]
myfriends.append("Ali")
print(myfriends)
myfriends.append(100)
print(myfriends)

# [2] Add List (as one element) to List 
myold = ["omar","ahmed","mohamed"]
mynew = ["one","Two","Three","Four"]
myold.append(mynew)
print(myold)    # Print : ['omar', 'ahmed', 'mohamed', ['one', 'Two', 'Three', 'Four']] => Add New List as One Element to Old List 
print(myold[3])     # Print : ['one', 'Two', 'Three', 'Four'] 
print(myold[3][1])     # Print : Two
print(myold[3][1:])     # Print : ['Two', 'Three', 'Four']

# [3] Extend() 
a =[1,2,3]
b =[4,5,6]
a.extend(b)
print(a)
c = ["omar","mohamed"]
a.extend(c)
print(a)

# [4] Remove()
# only match (remove) first element  
a = ["Omar","Ahmed","Ahmed"]
a.remove("Ahmed")
print(a)    # Print : ['Omar', 'Ahmed'] 

# [5] Sort() 
a = [10,1,5,3,-1,0,50,39]
a.sort()
print(a)
# a.sort(reverse=False) = a.sort()    # by default : Sort form A to Z 
a.sort(reverse=False)
print(a)

a.sort(reverse=True)        # Sort from Z to A
print(a)

c =["Omar","Mohamed","Ahmed","Ziad"]
c.sort()
print(c)
c.sort(reverse=True)
print(c)

# [6] Reverse()
p = [100,10,"Omar","Ahmed",1,5,2]
p.reverse()
print(p)