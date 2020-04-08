# -- coding: utf-8 --

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
mu, sigma = 0, 0.1 # mean and standard deviation
w = np.random.normal(0, 1, 1000)

for x in range(1000):
    
 print    (w[x])
 
 x=np.random.uniform(0,1,1000)
 
 y = [  1.2 + 2.3*x[n] +10 * w[n] for n in range(1000)]
 
 y = np.array(y)
 
 for n in range(1000):
     
    print(y[n])
    
    #pilotar grafico
    fig, ax = plt.subplots()
    ax.plot(x, y, '.')
    ax.grid(True, linestyle='-.')
    ax.tick_params(labelcolor='r', labelsize='medium', width=3)
    plt.show()

