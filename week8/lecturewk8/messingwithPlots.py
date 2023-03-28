# messing with MatPlotLib



import numpy as np                           # set up and import 
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))               # array not list
ypoints = xpoints * xpoints                  # y line = vertical

plt.plot(xpoints, ypoints, label= "xsquared")
plt.plot(xpoints, xpoints, label="straight", color="blue")
plt.legend()

randompoints = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, randompoints, label="random")

plt.show()

#plt.savefig('lecture1fig.png')