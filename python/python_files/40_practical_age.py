# ----------------------------------------
# ---------- Practical Age Full Details---
# ----------------------------------------

# age = input("What's Your Age?").strip()
# print(type(age))
# print(age)

# print("=" * 50)

# Convert age to integer value
# print(int(age))
# print(age)

# print("=" * 50)
# # or

age = int(input("What's Your Age?").strip())
# print(type(age))
# print(age)

# Get Age in all Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print("Your Lived For: ")
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")
