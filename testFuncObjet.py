import numpy as np
import matplotlib.pyplot as plt

class Display:
    """Clase que permite la graficación de las funciones objetivo y las
    poblaciones"""

    def f(self, t):
        """función objetivo que será graficada """
        x = 20 + np.exp(1) - 20 * (np.exp(-0.2 * abs(t)))- np.exp(np.cos(2*np.pi*t))
        return x

    def disp(self, x_min, x_max, tol):
        t1 = np.arange(x_min, x_max, tol)

        plt.plot(t1, self.f(t1), 'k',)
        plt.show()
