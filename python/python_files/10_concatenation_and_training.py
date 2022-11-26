# --------------------------
# Concatenation : concatenate string to another string
# Cannot concatenate string to number
# --------------------------

msg = "I love"
lang = "Python"
print(msg + lang)
print(msg + "  " + lang)

full = msg + " " + lang
print(full)

a = "First \
Second \
Third"

b = "a \
b \
c"
print(a + " " + b)
print(a + "\n" + b)

# print("Hello " + 1 )   # Error : cannot concatenate string to number
