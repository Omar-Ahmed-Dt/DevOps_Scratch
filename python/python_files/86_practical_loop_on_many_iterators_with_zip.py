# ----------------------------------------------------
# -- Practical => Loop on Many Iterators With Zip() --
# ----------------------------------------------------
# zip() Return A Zip Object Contains All Objects
# zip() Length Is The Length of Lowest Object
# ------------------------------------------------
from omar import seperator__ as sp

# list1 = [1, 2, 3]     # Length Is The Length of Lowest Object
list1 = [1, 2, 3, 4, 5]
list2 = ["Omar", "Osama", "Ali", "Mohamed", "Ahmed"]
ultimatelist = zip(list1, list2)
# print(ultimatelist)         # Print: <zip object at 0x0000023C25F4A800>

for item in ultimatelist:
    print(item)

sp()
for item1, item2 in zip(list1, list2):
    print("List 1  Item => ", item1)
    print("List 2  Item => ", item2)

sp()

tuple1 = ("Man", "Woman", "Girl", "Boy")
dict1 = {"Name": "Osama", "Age": 36, "Country": "Egypt", "Skill": "Python"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    print("List 1  Item => ", item1)
    print("List 2  Item => ", item2)
    print("Tuple 1  Item => ", item3)
    print("Dict 1  Key => ", item4, "Value => ", dict1[item4])
