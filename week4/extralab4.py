# Extra: get the program to generate a random number between 0 and 100 to guess.
# This program uses the random module in Python to generate a random number between 0 and 100 
# using the randint function. 
#It then prompts the user to guess the number and uses a while loop to repeatedly prompt the user 
#to guess again until they guess the correct number.
# author: Conor Tierney


import random     #import random generator

number = random.randint(0,100)                                 # define randon number between 1 and 100.
guess = int (input ("guess a number between 0 and 100:"))         # Prompt the user to guess the number

while guess != number:  
    if guess <number:
        print ("too low")
    else :                                   # Check if the guess is too low or too high 
        print ("too high")             
    guess = int(input("guess a number between 0 and 100:"))            # Prompt the user to guess again.

print ("well done you guessed the number: ", number)

# this works