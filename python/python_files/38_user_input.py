# --------------------
# -----User Input-----
# --------------------

fname = input("What's Your First Name? ")
mname = input('What\'s Your Middle Name? ')
lname = input('What\'s Your Last Name? ')

fname = fname.strip().capitalize()
# mname = mname.strip().capitalize()
# lname = lname.strip().capitalize()
print(f"Hello {fname} {mname.strip().capitalize():.1s} {lname.strip().capitalize()} Happy To See You...")
