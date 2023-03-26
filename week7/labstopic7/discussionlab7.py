# Create an “init” program that initializes the file, in this case it will just put 0
#into the file.

# Write some code to check if the file exists. To do this we will need to import
#os.path and use the isfile() function. 

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print ("file does not exist")

    writenumber(0)             #initialise file here


#Use a try catch loop on the read.

def readNumber():
     try:
         with open(filename) as f:
             number = int(f.read())
             return number
     except IOError:

        return 0                        