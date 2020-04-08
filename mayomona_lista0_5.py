# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 18:25:18 2020

@author: jones
"""

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.

x = np.arange(-10, 11, 0.25)
y = np.arange(-10, 11, 0.25)
Z = np.zeros((len(x),len(y)))
X, Y = np.meshgrid(x, y)
print(X.shape)
#Z = [ X[n]**2+Y[n]**2 for n in len(X)]
for n in range(0, len(x)):
    for i in range(0, len(y)):
        Z[n][i] = (X[n][i]**2+Y[n][i]**2) 

fig = plt.figure()
ax = fig.gca(projection='3d')

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()