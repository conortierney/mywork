# extra lab is even.
# modify program to deal with rounding number example 69.5 to 70% to deal with decimals.

#To explain the changes made to the original program:ifEven.py

# use the float() function to convert the user's input into a decimal number.
 #We then use the round() function to round the decimal number to the nearest integer.
# finally, we check if the rounded number is even or odd, and print out the result.
# ref: datacamp

# Get user input
num = round(float(input("Enter a decimal number: ")))

# Check if the number is even
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")

# test this**