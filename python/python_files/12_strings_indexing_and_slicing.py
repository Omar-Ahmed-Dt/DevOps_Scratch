# --------------------------
# Strings Indexing & Slicing
# 1 = All data in python is Object
# 2 = Object contain Elements
# 3 = Every element has its own Index
# 4 = Python use zero based Indexing ( index start from zero)
# 5 = Use square brackets to access element =>> []
# 6 = Enable accessing parts of strings, Tuples or Lists
# --------------------------

# Indexing ( Access Single Item ) :
mystring = "I love Python"
print(mystring[0])  # Index 0 => I
print(mystring[9])  # Index 9 => t
print(mystring[-1])  # Index -1 => First Character from End => n
print(mystring[-4])  # Index -4 => t

# ------------------------------------

# Slicing ( Access Multiple Sequence Items ) :
# [Start : End ] => End not included
# [Start : End : Steps]
slicing_string = "I love Python"
print(slicing_string[8:11])     # print : yth
print(slicing_string[2:6])      # print : love
print(slicing_string[3:5])      # print : ov

# If start is not here , will start from 0  :
# Print : I love Pyt
print(slicing_string[:10])
# If end is not here , will go to the end  :
# Print : Python
print(slicing_string[7:])
# If start and end are not here , will print all data  :
# Print : Full data
print(slicing_string[:])

# Slicing with Steps :
# By default is one step
# Print full data
print(slicing_string[::1])
# Print : Io tn
print(slicing_string[::3])