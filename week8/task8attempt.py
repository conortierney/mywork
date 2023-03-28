# Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2,
#and a plot of the function  h(x)=x3 in the range [0, 10],
#on the one set of axes.
# this uses the Numpy and Matplotlib libraries to genereate and display a histogram.

import numpy as np                           # numpy is np
import matplotlib.pyplot as plt             # matplot is ply

data = np.random.normal(5, 2, 1000)          # generate 1000 random numbers

plt.hist(data, bins=50, density=True)            # Plot a histogram of the data


plt.xlabel('Values')                             # Set the x-axis label
plt.ylabel('Frequency')                           # Set the y-axis label
plt.title('Histogram of Normal Distribution')       # Set the plot title
plt.show()                                          # Show the plot          



# density=True argument normalizes the histogram so that the area under the histogram is equal to 1.
#The histogram will have 50 bars, each representing a range of values from the minimum value to the 
#maximum value of the data, divided into 50 equally spaced bins. The height of each bar represents 
#the frequency of values that fall within that bin range. Since the distribution is normal, 
#the histogram will have a bell-shaped curve, with most values concentrated around the mean of 5