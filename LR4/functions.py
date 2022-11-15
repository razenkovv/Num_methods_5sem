import numpy as np


def f(x):
    return np.exp(np.sin(x/2)) - np.arctan(x) + 1


def diff_f(x):
    return 0.5*np.exp(np.sin(x/2))*np.cos(x/2) - 1/(x*x+1)

