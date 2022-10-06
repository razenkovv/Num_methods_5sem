import numpy as np
from matplotlib import pyplot as plt


def f(x):
    return np.arctan(np.sin(x))


def f_diff(x):
    return np.cos(x) / (np.power(np.sin(x), 2) + 1)


def f_diff_2(x):
    return -1 * (((np.power(np.sin(x), 2) + 2 * np.power(np.cos(x), 2) + 1) * np.sin(x)) / (
        np.power((np.power(np.sin(x), 2) + 1), 2)))


def error(x, y):
    #return np.mean(np.abs(x-y))
    #return np.median(np.abs(x - y))
    return np.max(np.abs(x - y))
