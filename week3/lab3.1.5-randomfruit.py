# This program prints out a random fruit
# Author : Conor T
#  Write a program (randomfruit.py) that prints out a random fruit.

import random
fruits = ['apple', 'orange', 'banana', 'pear']
# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))

# A Random Fruit:orange
#PS C:\Users\conor\OneDrive - Atlantic TU\pands\mywork\week3> python .\lab3.1.5-randomfruit.py    
#A Random Fruit:pear

#modify the program in 6 (randomFruit2.py) so that it uses a tuple ( ) not a list [ ].
#The functionality of the program will not change.