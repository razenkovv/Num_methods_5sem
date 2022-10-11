import numpy as np

import functions
from functions import f


def right_diff(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(0, x_node.size - 1):
        y_res[i] = (f(x_node[i + 1]) - f(x_node[i])) / h

    y_res[-1] = (f(x_node[-1]) - f(x_node[-2])) / h
    return y_res


def central_diff(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(1, x_node.size - 1):
        y_res[i] = (f(x_node[i + 1]) - f(x_node[i - 1])) / (2 * h)

    y_res[0] = (-3 * f(x_node[0]) + 4 * f(x_node[1]) - f(x_node[2])) / (2 * h)
    y_res[-1] = (3 * f(x_node[-1]) - 4 * f(x_node[-2]) + f(x_node[-3])) / (2 * h)
    return y_res


def second_diff_2(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(1, x_node.size - 1):
        y_res[i] = (f(x_node[i + 1]) - 2 * f(x_node[i]) + f(x_node[i - 1])) / (h * h)

    y_res[0] = (f(x_node[1]) - 2 * f(x_node[0]) + f(x_node[0] - h)) / (h * h)
    y_res[-1] = (f(x_node[-1] + h) - 2 * f(x_node[-1]) + f(x_node[-2])) / (h * h)
    return y_res


def second_diff_4(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(2, x_node.size - 2):
        y_res[i] = (-1*f(x_node[i + 2]) + 16*f(x_node[i + 1]) - 30*f(x_node[i]) + 16*f(x_node[i - 1]) - f(x_node[i - 2])) / (12 * h * h)

    y_res[1] = (-1*f(x_node[3]) + 16*f(x_node[2]) - 30*f(x_node[1]) + 16*f(x_node[0]) - f(x_node[0] - h)) / (12 * h * h)
    y_res[0] = (-1*f(x_node[2]) + 16*f(x_node[1]) - 30*f(x_node[0]) + 16*f(x_node[0] - h) - f(x_node[0] - 2*h)) / (12 * h * h)
    y_res[-1] = (-1*f(x_node[-1] + 2*h) + 16*f(x_node[-1] + h) - 30*f(x_node[-1]) + 16*f(x_node[-2]) - f(x_node[-3])) / (12 * h * h)
    y_res[-2] = (-1*f(x_node[-1] + h) + 16*f(x_node[-1]) - 30*f(x_node[-2]) + 16*f(x_node[-3]) - f(x_node[-4])) / (12 * h * h)
    return y_res
