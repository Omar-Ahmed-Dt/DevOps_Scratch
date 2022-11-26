# --------------------------------------------------
# -- File Handling --
# -------------------
# "a" Append  Open File For Appending Values, Create File If Not Exists
# "r" Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" Write   Open File For Writing, Create File If Not Exists
# "x" Create  Create File, Give Error If File Exists
# --------------------------------------------------

import os


def seperator_():
    print("#" * 50)


# [1] Relative Path
# Print Current Working Directory => C:\Users\omara\Documents\python
# Main Current Working Directory:
print(os.getcwd())

# Current Working Directory => C:\Users\omara\Documents\python\omar.txt
# file = open("omar.txt")

# [2] Absolute Path
# file = open("D:\omar.txt")

# Print Absolute Path for The Opened File
# Print: c:\Users\omara\Documents\python\65_handing_part1.py
print(os.path.abspath(__file__))

# Print Directory For The Opened File:
print(os.path.dirname(os.path.abspath(__file__)))

# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

seperator_()

# myfile = open("D:\noor.txt")   # Error \n  => new line
myfile = open(r"D:\noor.txt")
