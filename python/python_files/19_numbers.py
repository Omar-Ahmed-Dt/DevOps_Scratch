# -------------
# -- Numbers --
# -------------

# Integer

print(type(1))
print(type(100))
print(type(10))
print(type(-10))
print(type(-110))

# Float

print(type(1.500))
print(type(100.99))
print(type(-10.99))
print(type(0.99))
print(type(-0.99))

# Complex

myComplexNumber = 5+6j

print(type(myComplexNumber))
print("Real Part Is: {}".format(myComplexNumber.real))
print("Imaginary Part Is: {}".format(myComplexNumber.imag))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

# From int to float and complex
print(float(100))
print(complex(100))

# From float to int and complex
print(int(10.50))
print(complex(10.50))

# Cannt covert From complex to int and float
# print(int(10+9j))     # ERROR
# print(float(10+9j))   # ERROR
