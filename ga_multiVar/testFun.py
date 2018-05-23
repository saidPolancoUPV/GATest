import numpy as np

def fun1(x1, x2):
    y = 0.5 - (-0.5 + (np.sin(np.sqrt(x1 ** 2 + x2 ** 2)) ** 2)/(1.0 +
                                                                 0.001 * (
                                                                 x1 ** 2 +
                                                                 x2 ** 2) ** 2
                                                                 ))
    return y
