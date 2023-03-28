# make a scatter plot
#a list called ages that has, the same number random
#values as salaries, (range:21 to 65) .

# Author: Andrew Beatty

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# this is so that the "random" numbers are the same each time to make it easier to debug.
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high = 65, size = numberOfEntries) # I prefer putting the abolute values into variables that are set at the top

plt.scatter(ages, salaries ) 
plt.show()