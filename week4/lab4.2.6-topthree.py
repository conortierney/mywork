# This program generates 10 random numbers.
# prints them out, then
# prints out the top 3
# I will use a LIST to store and
# manipulate the numbers.
# append. a list
# sort. a list

import random

howmany = 10                 #program the case
tophowmany = 3
rangefrom = 0
rangeto = 100

numbers = []    #[] for lists

for i in range(0,howmany):
    numbers.append(random.randint(rangefrom,rangeto))
print (f"{howmany} random numbers\t {numbers}")

topones = numbers.copy()                  # I am keeping the original list maybe I don't need to???

topones.sort(reverse = True)
print ("The top {tophowmany} are \t\t {topones[0:tophowmany]}")

# this doesnt work for me **



