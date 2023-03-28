# This program is called plottask.py 
# Author : Conor Tierney.

# The program displays:
# 1) A histogram with a normal distribution of a 1000 values,
# with a  mean(loc) of 5 and standard deviation (scale) of 2.

# 2)Also, an exponential distribution function  h(x)=x3 in the range [0, 10],on the one set of axes.

# It uses the Numpy and Matplotlib libraries to genereate and display a histogram.

import numpy as np                               # import numpy as np as in labs.
import matplotlib.pyplot as plt                  # import matplot as ply as in labs.

data = np.random.normal(5, 2, 1000)              # This generates 1000 random numbers, 5 = mean, 2= Std

plt.hist(data, bins=50, density=True)            # Plot a histogram of the data


plt.xlabel('Values')                             # Set the x-axis label
plt.ylabel('Frequency')                          # Set the y-axis label
plt.title('plottask.py')                         # Set the plot title
plt.show()                                       # Show the plot          



