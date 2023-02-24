# floors a number.
#Write a program that takes in a float and outputs an int rounded
# down, you will need the math module math.floor()
# Math is a built in module
# Author: Conor T

import math
numbertofloor = float(input("Enter a float number:"))
floorednumber = math.floor(numbertofloor)

print ( '{} floored is {}'.format(numbertofloor, floorednumber))

#Enter a float number:11.99
#11.99 floored is 11