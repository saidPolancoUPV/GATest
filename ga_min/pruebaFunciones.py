import matplotlib.pyplot as plt
import numpy as np
from funTest import fun4 as f


t1 = np.arange(0.0, 25.0, 0.001)

t2 = [np.float(f(x)) for x in t1]
t3 = np.asarray(t2)

# print(t2)
plt.plot(t1, t3, 'k')
plt.show()
