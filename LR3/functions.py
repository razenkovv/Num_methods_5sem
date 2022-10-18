import numpy as np


def f(x):
    return np.tanh(x)


def f_integrate(x):
    return np.log(np.cosh(x))


def f_integral(s, e):
    return f_integrate(e) - f_integrate(s)


def error(x, y):
    return np.abs(x - y)
