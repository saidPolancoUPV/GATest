from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

# make data
X1 = np.arange(-10, 10, 0.25)
x2 = np.arange(-10, 10, 0.25)
X, Y = np.meshgrid(X1, x2)
Z = 0.5 - ((-0.5 + np.sin(np.sqrt(
    X ** 2 + Y ** 2)) ** 2) / (1.0 + 0.001 * (X ** 2 + Y ** 2) ** 2))

# plot the surface
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%0.2f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
