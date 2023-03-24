# Lab 4.1.1 | If, elif, else:
# Write a program (isEven.py) that asks the user to enter in a number, and the
# program will tell the user if the number is even or odd.
#**use this for task 4  - collatz.py


number = int(input ("enter an number:"))

if (number % 2) == 0:
    print (f"{number} is and even number")
else: 
    print (f"{number} is an odd number")

           
# Get user input
num = int(input("Enter a number: "))

# Check if the number is even
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
# second code found online. to test. 