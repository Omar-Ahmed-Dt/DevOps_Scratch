# ---------------------------------------------
# -----Membership Operators--------------------
# ----- in ------------------------------------
# ----- not in --------------------------------
# ---------------------------------------------

# String
name = "Omar"
print("m" in name)      # Print: True
print("r" in name)      # Print: True
print("o" in name)      # Print: False

print("#" * 50)

# List
friends = ["Omar", "Mohamed", "Anas"]
print("Omar" in friends)
print("Ali" in friends)         # Print: False
print("Ali" not in friends)     # Print: True

print("#" * 50)

# Using (in) and (not in) with condition
countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "Russia"]
countriesTwoDiscount = 50

myCountry = input("Enter Your Country ").strip().capitalize()

if myCountry in countriesOne:
    print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")
elif myCountry in countriesTwo:
    print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")
else:
    print("You Have No Discount")
