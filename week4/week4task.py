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


n = int(input("Please enter a positive integer: ")) # ask user to input a positive integer

while n != 1:                                # while n is not equal to 1
    print(n, end=" ")                       # print the value of n followed by a space
    if n % 2 == 0:                          # if n is even
        n = n // 2                          # divide n by 2
    else:                                   # if n is odd
        n = 3 * n + 1                         # multiply n by 3 and add 1

print(n,end=" ")                                    # print the final value of n, which is always 1
