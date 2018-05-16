import matplotlib.pyplot as plt
from numpy import arange
from funTest import fun4 as f


t1 = arange(0.0, 10.0, 0.001)

plt.plot(t1, f(t1), 'k')
plt.show()
