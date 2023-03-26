# Write a program that counts how many times it was run.
# Write a function that reads in a number from a file that already exists
# test the program by calling the function and outputting the number.

# a
FILENAME = "count.txt"                 
def readNumber():
  with open(FILENAME) as f:
     number = int(f.read())
     return number
'''
num = readNumber()               # test it, it workes= 0
print (num)'''


# b- Write a function that takes in a number and overwrites a file with that number (count.txt).

def writeNumber(number):
 with open(FILENAME, "wt") as f: 

   f.write(str(number))                         # write takes a string so we need to convert

'''# test it
writeNumber(3)                 # this changes count.txt to 3'''

# main program
num = readNumber()
num += 1
print (f"we have run this program {num} times")
writeNumber(num)

# output = +1 everytime program is ran.