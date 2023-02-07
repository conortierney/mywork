# task2.py
# Author: Conor
# trial task2, adding cents and total in euro
# example follow lab as example / bank.py

amt1 = int(input("enter amount1(in cents):"))
print (f"the amount is {amt1}")

amt2 = int(input("enter amount2(in cents):"))
print (f"the amount is {amt2}")

amttotal  = (amt1 + amt2)/100

print (f"the sum of these is: €{amttotal}")

