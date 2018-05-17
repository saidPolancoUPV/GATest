import numpy as np
import matplotlib.pyplot as plt
from funTest import fun4 as f


class Display:
    """Clase que permite la graficación de las funciones objetivo y las
       poblaciones"""

    def disp(self, x_min, x_max, tol, pob):
        t1 = np.arange(x_min, x_max, tol)

        plt.plot(t1, f(t1), 'k', np.asarray(pob[0]), np.asarray(pob[1]),
                 'bo')
        plt.show()
