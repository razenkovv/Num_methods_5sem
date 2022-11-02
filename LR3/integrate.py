import numpy as np

from functions import f


def rectangle_method(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(0, x_node.size):
        y_res[i] = f(x_node[i])
    return y_res.sum() * h


def trapz_method(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(0, x_node.size - 1):
        y_res[i] = 0.5 * (f(x_node[i]) + f(x_node[i + 1])) * h
    return y_res.sum()


def simpson_method(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(1, x_node.size - 1, 2):
        y_res[i] = (f(x_node[i - 1]) + 4 * f(x_node[i]) + f(x_node[i + 1])) * (h / 3)
    return y_res.sum()
