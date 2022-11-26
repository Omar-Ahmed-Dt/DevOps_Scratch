# -----------------------------------
# --      Exceptions Handling      --
# -- Try | Except | Else | Finally --
# -----------------------------------
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# ----------------------------
# Else    => If No Errors
# Finally => Run The Code
# ------------------------
from omar import seperator__ as sp
try:        # Try The Code and Test Errors
    age = int(input("Enter Your Age: "))
    # print("Good, This is Integer From Else.")

except:     # Handle The Errors If Its Found

    print("This is Not Integer.")
else:  # If Theres No Errors
    print("Good, This is Integer From Else.")

finally:
    print("Print From Finally Whatever Happens")

sp()

# Example 
try:

  print(10 / 0)
#   print(x)
#   print(int("Hello"))

except ZeroDivisionError:

  print("Cant Divide")

except NameError:

  print("Identifier Not Found")

except ValueError:

  print("Value Error Elzero")

except:

  print("Error Happens")
