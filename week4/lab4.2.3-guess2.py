# modify last program guess1 so program tells user if guess is too high/low.
# this program uses and IF statement instead of a WHILE loop.
# this is example of while, if , else statements.

numbertoguess = 25              

guess = int (input ("please guess a number:"))  
while guess != numbertoguess:  
    if guess <numbertoguess:
        print ("too low")
    else :                                   # cannot be equal or too low, so it must be too high# 
        print ("too high")             
    guess = int(input("guess again:"))           
     
print ("well done the number was: ", numbertoguess)