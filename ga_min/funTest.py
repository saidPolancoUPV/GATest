import numpy as np
import bigfloat


def fun1(x):
    y = 1 + (np.cos(x) / (1 + 0.01 * x ** 2))
    return y


def fun2(x):
    y = -1 * (np.absolute(x * np.sin(np.sqrt(np.absolute(x)))))
    return y


def fun3(x):
    y = np.sin(x) / (1 + np.sqrt(x) + (np.cos(x) / (1 + x)))
    return y


def fun4(x):
    # np.seterr(all='ignore')
    with bigfloat.precision(10):
         y = 5 + bigfloat.exp(0.5 * np.cos(np.pi * x ** 2)) - bigfloat.exp(
                                  0.1 * x * np.cos(np.pi * x))
    print(y)
    return y
