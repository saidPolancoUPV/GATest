import numpy as np
import matplotlib.pyplot as plt


def f(t):
    x = 20 + np.exp(1) - 20 * (np.exp(-0.2 * abs(t)))- np.exp(np.cos(2*np.pi*t))
    return x

t1 = np.arange(0.0, 32.0, 0.1)

plt.plot(t1, f(t1), 'k')
plt.show()
