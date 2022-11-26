# ----------------------------------
# -----Calculate Age A.V------------
# ----------------------------------

age = int(input(" => Please Enter Your Age ").strip())

# Write note
# print(" =>>> You Can Write First Litter or Full Word Of The Time Unit <<<= ")
print("#" * 80)
print(" You Can Write First Litter or Full Word Of The Time Unit ".center(80, "#"))
print("#" * 80)

# Choose Time Unit
unit = input(
    " => Choose Unit For Calculate Your Age: Months, Weeks, Days: ").strip().lower()

months = age * 12
weeks = months * 4
days = age * 365

if unit == "months" or unit == "m":
    print("You Choosed The Unit Months")
    print(f"You Lived For {months:,} Months.")
elif unit == "weeks" or unit == "w":
    print("You Choosed The Unit Weeks")
    print(f"You Lived For {weeks:,} weeks.")
elif unit == "days" or unit == "d":
    print("You Choosed The Unit Days")
    print(f"You Lived For {days:,} Days.")
else:
    print("Not Understand You !!")
