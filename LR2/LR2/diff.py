import numpy as np

import functions
from functions import f


def right_diff(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(0, x_node.size - 1):
        y_res[i] = (f(x_node[i + 1]) - f(x_node[i])) / h
    y_res[x_node.size - 1] = (f(x_node[x_node.size - 1]) - f(x_node[x_node.size - 2])) / h
    return y_res


def central_diff(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(1, x_node.size - 1):
        y_res[i] = (functions.f(x_node[i + 1]) - functions.f(x_node[i - 1])) / (2 * h)
    y_res[0] = (-3 * functions.f(x_node[0]) + 4 * functions.f(x_node[1]) - functions.f(x_node[2])) / (2 * h)
    y_res[x_node.size - 1] = (3 * functions.f(x_node[x_node.size - 1]) - 4 * functions.f(
        x_node[x_node.size - 2]) + functions.f(x_node[x_node.size - 3])) / (2 * h)
    return y_res


def second_diff_2(x_node):
    h = x_node[1] - x_node[0]
    y_res = np.zeros(x_node.size)
    for i in range(1, x_node.size - 1):
        y_res[i] = (functions.f(x_node[i + 1]) - 2 * functions.f(x_node[i]) + functions.f(x_node[i - 1])) / (h * h)

    y_res[0] = (functions.f(x_node[1]) - 2 * functions.f(x_node[0]) + functions.f(x_node[0] - h)) / (h * h)
    y_res[x_node.size - 1] = (functions.f(x_node[x_node.size - 1] + h) - 2 * functions.f(x_node[x_node.size - 1]) + functions.f(x_node[x_node.size - 2])) / (h * h)
    return y_res

# def second_diff_4(x_node):
#     h = x_node[1] - x_node[0]
#     y_res = np.zeros(x_node.size)
#     for i in range(1, x_node.size - 1):
#Доделать
