# program that reads in two numbers and
# outputs the integer answer and remainder
# Write a program (div.py) that reads in two numbers and
# divides the first one by the second and give the integer result and the
# remainder

x = int (input ("enter first number: "))
y = int (input ("enter the number to divide by: "))
answer = int (x//y)   # // gives the int division
remainder = x%y       # % gives the remainder

print ("{} divided by {} is {} with remainder {}".format (x, y, answer, remainder))

# result
# enter first number: 10
# enter the number to divide by: 3
# 10 divided by 3 is 3 with remainder 1