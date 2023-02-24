#Write a program
#called convert.py that takes in a float amount of dollars and returns that
#absolute amount in cent.

numbertoconvert = float(input("enter an amount"))
convertedtocents = int (numbertoconvert)

print ( '{} that amount in cents is{}'.format(numbertoconvert,convertedtocents))

# this is not CORRECT output

amount = 5.99
ascent = amount * 100
print (f"{amount} as cent is {ascent}")