# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

cName = "Python Course"
cPrice = 100

uName = input("Enter Your Name: ").strip().capitalize()
uCountry = input("Enter Your Country: ").strip().capitalize()

if uCountry == "Egypt":
    print(f"Hello {uName},The course \"{cName}\" Price Is ${cPrice - 80}")
elif uCountry == "Russia":
    print(f"Hello {uName},The course \"{cName}\" Price Is ${cPrice - 60}")
else:
    print(f"Hello {uName},The course \"{cName}\" Price Is ${cPrice - 30}")
