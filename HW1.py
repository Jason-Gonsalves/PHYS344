##Plotting Random Coordinates Pairs##

from __future__ import division
from pylab import *
from numpy import *

import random

X = np.floor(100*np.random.rand(10)) #Creates 10 random X coordinates between 0 and 100
Y = np.floor(100*np.random.rand(10)) #Creates 10 random Y coordinates between 0 and 100

plt.scatter(X,Y)
plt.show()


