# ref - https://www.youtube.com/watch?v=neuNX44cMbg
# collatz conjecture, collatz.py
# Author : Conor Tierney.
# ask user to input a positive integer stored as "number"
# while n is not equal to 1.
# at each stage of the loop, the program updates the number value based on whether it is even or odd.
# if n is even, divide // n by 2.
# if n is odd, x n by 3 and + 1.
# when number becomes 1, the loop ends. 
# make sure to print output on same line
# this is correct..


number = int(input("Please enter a positive number: ")) 

while number < 1:
        print (number, ":isn't a positive number.")
        number = int(input ("Enter a positive number: "))           
       
                            
print(number, end=" ")                       

while number > 1:
    if number % 2 == 0:                          
        number = number // 2                          
        print (number ,end = " ")
    else:                                   
        number = 3 * number + 1                        
        print (number,end = " ")  
