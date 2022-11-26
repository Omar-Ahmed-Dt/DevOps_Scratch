# -----------------------------------------------
# ---- File Handling => Write and Append --------
# -----------------------------------------------

file = open(r"D:\omar.txt", "w")
# file.write(
#     "Hello This Is Test For Loops In Files Flying Away A Bird also Flies Wow \n" * 100)
mylist = ["Omar\n", "Ahmed\n", "Mohamed\n"]
file.writelines(mylist)

file = open(r"D:\omar.txt", "a")
# file.write("Hello Omar \n")
file.write("Hello Python\n\n\n\n")
file.write("Hello ~!!!")
