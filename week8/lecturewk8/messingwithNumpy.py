# Messsing with numpy
# Author: Andrew Beatty
# see read me files on github
# w3 schools see Numpy tutorial- creat arrays// numpy website


import numpy as np         # import as np

list_of_numbers= [1,2,3,"asdf"]                         # this is a list,1,2,2 etc
list_of_numbers = list_of_numbers + [3]                 # does not work to add to list
print ("list", list_of_numbers)

numbers = np.array([1,2,3,4])                  # numpy works by storing only one variable type#
numbers = numbers + 3                          
numbers = numbers * [1,2,3,5 ]                # can add or multiply lists

print("array", numbers)          


# creating random numbers
rando = np.random.randint(100,200,30)                     # randon integer/ n=30 nos. between 100 and 200
print(rando)
normalrando = np.random.normal(loc= 50, scale= 20, size=100)       # normal randon for stats  - for mean and SD
print (normalrando)                                                    # see normal dist in w3 schools