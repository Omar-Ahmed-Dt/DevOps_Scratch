# ------------------------
# ---Strings Formatting---
# Olde Method => New Method :
# %s => {}
# % variable => .format(variable)
# %(var1,var2,var3) => .format(var1.var2.var3)
# {:s} => String
# {:d} => Digit
# {:f} => Float
# ------------------------

# [1] New Method :
name = "Omar"
age = 24
rank = 30
print("My Name is: {} and My Age is: {} and My Rank is: {}".format(name, age, rank))
print("My Name is: {:s} and My Age is: {:d} and My Rank is: {:f}".format(
    name, age, rank))

# [2] Control Floating Point Number
a = 30
print("Value of a: {:f}".format(a))
print("Value of a: {:.2f}".format(a))
print("Value of a: {:.10f}".format(a))

# [3] Truncate String
mylongstring = "Hello People of Programming World I Love all"
print("Message is : {:s}".format(mylongstring))
print("Message is : {:.5s}".format(mylongstring))
print("Message is : {:.12s}".format(mylongstring))

# [4] Format Money
mymoney = 500340120234
print("My Money is {:d}".format(mymoney))
print("My Money is {:_d}".format(mymoney))
print("My Money is {:,d}".format(mymoney))
# print("My Money is {:&d}".format(mymoney))      # Wrong When Using &

# [5] ReArrange Items
a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))     # Print : Hello One Two Three
print("Hello {1} {2} {0} ".format(a, b, c))     # Print : Hello Two Three One

A, B, C = 10, 20, 384533
print("My Numbers are {2:.2f} {0:d} {1:.4f} ".format(A, B, C))

# [6] Format in Version 3.6+
name = "Omar"
age = 24
print("My Name is {name} and My Age is {age}")
print(f"My Name is {name} and My Age is {age}")
