# ------------------------------------
# ---- Simple Bookmark manager -------
# ------------------------------------

# Creat Empty List
mylist = []
# Maximum Webs Numbers
maximumwebs = 5

while maximumwebs > 0:
    web = input("Enter Name Web Without https:// ")
    mylist.append(f"https://{web.strip().lower()}")
    maximumwebs -= 1
    print(f"Website Added, {maximumwebs} Places Left")
    # print(mylist)
else:
    print("Your Bookmark Is Full Now")

# Check IF List not empty
if len(mylist) > 0:
    mylist.sort()
    index = 0
    print("Printing The BookMark..")
    while index < len(mylist):
        print(mylist[index])
        index += 1
