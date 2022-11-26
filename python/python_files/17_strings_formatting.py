# ------------------------
# ---Strings formatting---
# ------------------------
# Concatenating and Formating for Strings :

# [1] Concatenating :
name = "Omar"
age = 24
rank = 30
print("My Name is : " + name)
# print("My Name is : " + name + " My Age is : " + age )    # Type Error => can only concatenate str to str

# [2] Formating :
# Place_holder [%s and %d and %f ] to solve concatenating problem :
# %s : String && %d : Digital [Number] && %f : Float
print("My Name is : %s" % "Omar")
print("My Age is : %s" % age)
print("My Name is : %s and My Age is : %s" % (name, age))
print("My Name is : %s and My Age is : %d and My Rank is : %f" % (name, age, rank))

# [3] Control Floating Point Number :
mynum = 10
print("MY Number is : %d" % mynum)
print("My Number is : %f" % mynum)
print("My Number is : %.2f" % mynum)    # %.2f => 10.00
print("My Number is : %.4f" % mynum)    # %.4f => 10.0000

# [4] Truncate string :
mylongstring = "Hello People of Programming World I Love all"
print("Message is %s" % mylongstring)
print("Message is %.12s" % mylongstring)    # Print : Message is Hello People
