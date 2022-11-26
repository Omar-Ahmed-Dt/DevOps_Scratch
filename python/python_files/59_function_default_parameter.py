# ------------------------------------
# ---- Function Default Parameter-----
# ------------------------------------

# Default parameter Must be Last Value in Function :
# def say_hello(name="Unknown", age, country):      # Error
# def say_hello(country, age, name="Unknown"):      # Right

def say_hello(name="Unknown", age="Unknown", country="Unknown"):

    print(f"Hello {name} Your Age is {age} and Your Country Is {country}")


say_hello("Osama", 36, "Egypt")
say_hello("Mahmoud", 28, "KSA")
# Print: Hello Sameh Your Age is 38 and Your Country Is Unknown :
say_hello("Sameh", 38)
say_hello("Ramy")
say_hello()         # print: Hello Unknown Your Age is Unknown and Your Country Is Unknown
