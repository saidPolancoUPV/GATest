import numpy as np


def fun1(x1, x2):
    y = 0.5 - ((-0.5 + np.sin(np.sqrt(
        x1 ** 2 + x2 ** 2)) ** 2) / (1.0 + 0.001 * (x1 ** 2 + x2 ** 2) ** 2))
    return y


def fun2(x):
    nvar = len(x)
    nsum = 0
    for i in range(0, nvar):
        nsum += x[i] ** 2 - 10 * np.cos(2 * np.pi * x[i])

    r = 10 * nvar + nsum
    return r


def fun3(x):
    nvar = len(x)
    nsum = 0
    for i in range(0, nvar):
        nsum += np.sin(x[i]) * np.sin(((i+1) * x[i] ** 2)/(np.pi)) ** 20
    r = -nsum

    return r


def fun4(x):
    nvar = len(x)
    nsum = 0
    for i in range(0, nvar):
        nsum += -1 * x[i] * np.sin(np.sqrt(np.absolute(x[i])))
    r = nsum

    return r
