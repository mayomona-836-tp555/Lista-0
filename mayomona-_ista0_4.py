# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:14:18 2020

@author: jones
"""


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

x = np.random.uniform(0,1,10000)

y= np.random.uniform(0,1,10000)
 
z = [ x[n]+y[n] for n in range(10000)]
 

for n in range(1000):
     
    print(z[n])
    num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(z, num_bins, density=1)


ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()