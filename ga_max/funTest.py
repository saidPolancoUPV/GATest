import numpy as np


def fun1(x):
    y = 20 + np.exp(1.0) - 20 * (np.exp(-0.2 * abs(x))) - np.exp(
        np.cos(2 * np.pi * x))
    return y


def fun2(x):
    y = (np.sin((5 * np.pi * x))) ** 6 * np.exp((-2 * np.log(
        2) * (((x - 0.1) / 0.8) ** 2)))
    return y


def fun3(x):
    y = x + np.absolute(np.sin(32 * np.pi * x))
    return y


def fun4(x):
    y = 0.5 - ((np.sin(x) ** 2 - 0.5) / (1 + 0.001 * x ** 4))
    return y
