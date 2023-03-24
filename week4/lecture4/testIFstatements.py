# program to show the format of an IF statement.

# format of an if statement #1
# if condition:
# statements

# if condition:  #2
# statements(if true)
# else:
#   statements(if false)

# if condition1:
#  statements(if true)
#elif condition2:         #3
#  statemets (if condition1 is false but 2 is true)
# else:
#  statemetns(if both are false).

b =1
if True: 
    print("here we have if statement") # 1 :if true or if false statements e.g.
    b = 2

c = 1
if c == 1:
 print ("c is one")
else:
   print ("c is not one")  # 2: if/ else statements, true/false.

d = 4
if d < 0:
 print("d is negative")
elif d > 10:                 # 3 elif
 print ("d is 10 or more")
else:
   print ("d is between 0 and 9(inclusive)")

print ("sanity", d)

# play around here with numbers and <,>, <=, >=.