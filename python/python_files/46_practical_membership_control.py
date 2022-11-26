# ------------------------------------------------
# -------- Practical Membership Control ----------
# ------------------------------------------------

# List Contains Admins
admins = ["Ahmed", "Omar", "Osama", "Sameh",
          "Manal", "Rahma", "Mahmoud", "Enas"]

# print(admins)
# print(admins.index("Omar"))       # Print: 1
# print(admins[1])                  # Print: Omar
# admins[admins.index("Omar")] = "Ali"
# print(admins)

# Login
name = input("Enter Enter Your Name ").strip().capitalize()

# If Name Is In Admin
if name in admins:
    print(f"Hello {name}, Welcome Back.")
    option = input("Delete or Update Your Name ? ").strip().capitalize()
    # Update Option
    if option == "Update" or option == "U":
        newname = input("Enter Your New Name: ").strip().capitalize()
        admins[admins.index(name)] = newname
        print("Name Updated.")
        print(admins)
    # Delete Option
    elif option == "Delete" or option == "D":
        admins.remove(name)
        print("Name Deleted.")
        print(admins)
    # Wrong Option
    else:
        print("Wrong Option!")

else:
    print("You Are Not Admin")
    status = input(
        "Not Admin, Are You Want Add To Admin Y | N ? ").strip().capitalize()
    if status == "Yes" or status == "Y":
        admins.append(name)
        print("You Have Been Added.")
        print(admins)
    else:
        print("You Are Not Added.")
