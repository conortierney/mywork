# messing with Histograms.py

import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(1)                      # this runs random seed data/ need big enough set to run

normData = np.random.normal(size=10000)             # get random data/ normal distribution
plt.hist(normData)                                   # make a historgram of the above
plt.show()

'''
fruit = np.array(['Apples', 'Orange', 'Banana'])          # array/ not list
numbers = np.array([23,77,500])

plt.pie(numbers, labels = fruit)                       # makes pie chart w labels
plt.legend()
plt.show()
'''