import numpy as np


def tdma(left, right):
    """
    TriDiagonal Matrix Algorithm\n
    Решение СЛАУ с трехдиагональной матрицей. Важно диагональное преобладание.\n
    :param left: массив значений в левой части матрицы (все ненулевые элементы подряд построчно)
    :param right: правая часть матрицы
    :return: массив решений
    """
    n = 3
    if len(left) != (len(right) - 2) * n + 4:
        raise Exception("tdma method: something wrong with input\n")
    a_coef = np.zeros(len(right))
    b_coef = np.zeros(len(right))
    a_coef[0] = right[0] / left[0]
    b_coef[0] = -1 * left[1] / left[0]
    ind = n
    for i in range(1, len(right) - 1):
        a_coef[i] = (right[i] - left[ind - 1] * a_coef[i - 1]) / (left[ind] + left[ind - 1] * b_coef[i - 1])
        b_coef[i] = -1 * left[ind + 1] / (left[ind] + left[ind - 1] * b_coef[i - 1])
        ind += n
    a_coef[-1] = (right[-1] - left[ind - 1] * a_coef[-2]) / (left[ind] + left[ind - 1] * b_coef[-2])
    b_coef[-1] = 0.0

    res = np.zeros(len(right))
    res[-1] = a_coef[-1]
    for i in range(len(res) - 2, -1, -1):
        res[i] = a_coef[i] + b_coef[i] * res[i + 1]
    return res


def make_system(p, q, f, lft, rgt, nodes, order=1):
    if len(np.unique(np.diff(nodes).round(10))) != 1:
        raise Exception("make_system: grid must be uniform")
    h = nodes[1] - nodes[0]
    n = 3
    left = np.zeros((len(nodes) - 2) * n + 4)
    right = np.zeros(len(nodes))
    ind = n
    for i in range(1, len(nodes) - 1):
        left[ind - 1] = 1 - p(nodes[i]) * h / 2
        left[ind] = -2 + h * h * q(nodes[i])
        left[ind + 1] = 1 + h * p(nodes[i]) / 2
        right[i] = h * h * f(nodes[i])
        ind += n
    if order == 1:
        left[0] = lft[1] * h - lft[0]
        left[1] = lft[0]
        right[0] = lft[2] * h
        left[-2] = -1 * rgt[0]
        left[-1] = rgt[0] + h * rgt[1]
        right[-1] = rgt[2] * h
    elif order == 2:
        if lft[0] != 0:
            left[0] = -2 + 2 * h * lft[1] / lft[0] - p(nodes[0]) * lft[1] * h * h / lft[0] + q(nodes[0]) * h * h
            left[1] = 2
            right[0] = h * h * f(nodes[0]) + 2 * h * lft[2] / lft[0] - p(nodes[0]) * lft[2] * h * h / lft[0]
        else:
            left[0] = lft[1]
            left[1] = 0
            right[0] = lft[2]
        if rgt[0] != 0:
            left[-2] = 2
            left[-1] = -2 - 2 * h * rgt[1] / rgt[0] - p(nodes[-1]) * h * h * rgt[1] / rgt[0] + q(nodes[-1]) * h * h
            right[-1] = f(nodes[-1]) * h * h - 2 * h * rgt[2] / rgt[0] - p(nodes[-1]) * h * h * rgt[2] / rgt[0]
        else:
            left[-2] = 0
            left[-1] = rgt[1]
            right[-1] = rgt[2]
    else:
        raise Exception("make_system: only 1st or 2nd order")

    return left, right
