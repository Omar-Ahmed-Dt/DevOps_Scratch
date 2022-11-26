# ---------------------------------------
# ---- Simple Password Guess ------------
# ---------------------------------------

tries = 4

mainpass = "omar@123"

pass_ = input("Enter Your Password: ")

while pass_ != mainpass:
    tries -= 1
    # print(f"Wrong Password !, {tries} Chances Left ")
    print(
        f"Wrong Password, { 'Last' if tries == 0 else tries} Chances Left ")
    pass_ = input("Enter Your Password: ")
    if tries == 0:
        print("All Tries Is Finished")
        break
else:
    print("Successful Password")
