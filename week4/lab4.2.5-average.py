# this program reads in numbers
# until user enters 0
# it will then print back out again
# and their average

numbers = []

number = int(input("enter number (0 to quit): "))  # enterfirst number then we check if it is 0 in the while loop.

while number != 0:
 numbers.append(number)
 number = int(input("enter another (0 to quit): "))  #read the next number and check if 0

for value in numbers:
 print (value)

average = float(sum(numbers)) / len(numbers)           # I want average to be a float

print (f"The average is {average}")