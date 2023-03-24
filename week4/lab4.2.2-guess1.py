# program that prompts the user to guess a number, the program should keep prompting the user to 
# guess the number until the user gets the correct one. 
# guess.py


numbertoguess = 25              # define number

guess = int (input ("please guess a number:"))  # te; user to guess number
while guess != numbertoguess:                   # while loop, print wrong ! if not 25
    print ("wrong")
    guess = int(input("guess again:"))            # prompt user to keep guessing until correct.
     
print ("well done the number was: ", numbertoguess)


