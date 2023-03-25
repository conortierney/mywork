# messing with operating system OS
# use this for task 7 attempt ref

import os

filename  = "messingwithfiles.py"           # I am assuming that os is already imported

if os.path.exists(filename):
    with open(filename, "r") as f:
        for line in f:
             print (line, end="")
else:
    print(filename, "does not exist do you want to create it?")
    

# os.remove("dara2.txt")    # this function removes a file