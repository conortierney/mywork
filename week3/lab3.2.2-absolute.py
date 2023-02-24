# Give the absolute value of a number
# Enter a number:-4
# The absolute value of -4.0 is 4.0
#Author: Conor T
# In the question, number is ambiguous but the
# output implies that we should be dealing with floats
# So I am casting the input to a float

number = float(input("enter a number"))
absolutevalue = abs (number)
print ('the absoulute value of{} is{}'.format(number,absolutevalue))



