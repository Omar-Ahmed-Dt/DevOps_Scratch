# --------------------
# ----Nested IF-------
# --------------------

cName = "Python Course"
cPrice = 100

uName = input("Enter Your Name: ").strip().capitalize()
uCountry = input("Enter Your Country: ").strip().capitalize()
isStudent = input("Are You Student?").strip()

if uCountry == "Egypt" or uCountry == "Russia":
    if isStudent == "yes":
        print(
            f"Hello {uName},Because Your are from \"{uCountry}\" and Student The course \"{cName}\" Price Is ${cPrice - 80}")
    else:
        print(
            f"Hello {uName},Because Your are From \"{uCountry}\", The course \"{cName}\" Price Is ${cPrice - 50}")
else:
    print(f"Hello {uName},The course \"{cName}\" Price Is ${cPrice - 30}")
