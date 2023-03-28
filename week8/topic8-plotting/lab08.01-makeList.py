#This is just to show you numpy exists
# salaries
# Author: Andrew Beatty
# numpty

import numpy as np
# it is a good idea to have your absolute values set into variables at the
#beginning of your program.

minSalary= 20000
maxSalary = 80000
numberOfEntries = 10

np.random.seed(1)           # this seed (1) is so that the "random" numbers are the same each time to make it easier to debug.
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print (salaries)

# add 5000 to each entry
salariesPlus = salaries + 5000                   # matrix operations
print(salariesPlus)

# you can also multiply 
salariesMult = salaries * 1.05                    # add 5% by mulitplying by 1.05
print(salariesMult)
# this is a float array to convert to an int array (it does a float)
newSalaries = salariesMult.astype(int)
print(newSalaries)
