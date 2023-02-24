# Built in functions with numbers
# rounds a number
# be careful of round, it rounds to the nearest even number
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# so do not use it accuracy is essential
# Author: Conor T

numbertoround = float(input("enter a float number"))
roundednumber = round(numbertoround)
print ( '{} rounded is {}'.format(numbertoround,roundednumber))

#enter a float number4.5
#4.5 rounded is 4