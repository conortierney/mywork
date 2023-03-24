# task 5 - practice
# weekday.py 
#Write a program that outputs whether or not today is a weekday.
# example : "Yes, unfortunately today is a weekday"
# program gets the current date and time using the ' datetime.datetime.today()' function.
# and then uses the  'weekday' method to get the day of the week as an integer (<5)0mon-6 sun. 
# potential ref: https://www.youtube.com/watch?v=704PTqj1_W4
# search date time module how to complete this task.
# reference  https://docs.python.org/3/library/datetime.html


import datetime  # use import function  - see python built in functions.

today = datetime.datetime.today().weekday()     # define today

if today < 5:                          # 0 = Monday, 1 = Tuesday, ..., 4 = Friday ||| # 2 - IF statement.
    print("Oh no, today is a weekday, sorry.")
else:                                               # else statement.
    print("Happy days, today is a weekend day.")

# change " text for outputs"