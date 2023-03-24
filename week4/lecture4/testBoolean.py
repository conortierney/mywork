# week 4 
# messing with booleans, can be True or False
# boolean is the return type of the mathematical operators
# =, <, >, <=, >=, !=
# flipped with NOT keyword
# carefule using AND, OR
# Author: Conor Tierney
# these are statements = see other example for (f"xyz{xyz}") function in past weeks  =prints the "" statement.

conor_is_alive = True
print (f"conor is alive = {conor_is_alive}")

var = (2 == 4) # brackets make this easier to read, != is NOT equal to. 
print (f" var is = {var}")

logic  = (2<= 100) or (3 >=100) #is 2 less than or = 100(no), is 3 >=100(true), AND/OR.
print (f"logic is {logic}")
# use AND or OR here.

grade  = 400
invalid  = (grade <0) or (grade  >100)
print (f"invalid is {invalid}")  # this is called invalid. / change it to 40 see what happens. 