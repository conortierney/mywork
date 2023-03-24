# program to print all the even numbers from 2 to 100.
# this is a while loop.
# evens.py 
# Author: Conor Tierney

numberto = 100   # 1st way
evennum = 2

while evennum <= numberto:
    print (evennum)
    evennum += 2

    
number = 2    #second way

while number <= 100:
    print(number)
    number += 2

# we initialize the variable num to 2, which is the first even number we want to print.
# use a while loop to continue printing even numbers until we reach 100.
# Inside the loop, we print the current value of num and then increment it by 2 using the += operator.
# This ensures that we only print even numbers.