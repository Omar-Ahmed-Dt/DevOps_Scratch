# ----------------------------------------------
# ----- File Handling => Read File -------------
# ----------------------------------------------
def seperator_():
    print("#" * 50)


myFile = open("D:\omar.txt", "r")
# myFile = open("D:\omar.txt")     # Default Value => Read
print(myFile)  # File Data Object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

seperator_()

# print(myFile.read())
# print(myFile.read(5))       # Read 5 Characters Only
# seperator_()
# print(myFile.readline())    # Read All Line
# seperator_()
# print(myFile.readlines())       # Read All Lines and Return Output As List

for line in myFile:
    print(line)
    if line.startswith("For"):
        break

# Close The File:
myFile.close()
