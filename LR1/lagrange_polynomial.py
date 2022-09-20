import numpy as np


def calc(arg, _x, _y, n):
    res = 0
    for _i in range(0, n, 1):
        m1 = 1
        m2 = 1
        for _j in range(0, n, 1):
            if _i != _j:
                m1 *= (arg - _x[_j])
                m2 *= (_x[_i] - _x[_j])
        res += _y[_i] * (m1 / m2)
    return res


def create_cheb_nodes(s, e, n):
    x_cheb_node = np.zeros(n)
    for k in range(0, n, 1):
        x_cheb_node[k] = 0.5 * (e + s) + 0.5 * (e - s) * np.cos((2 * k + 1) * np.pi / (2 * n))
    x_cheb_node = np.sort(x_cheb_node)
    return x_cheb_node


def create_test_x(s, e, n):
    x_res = np.zeros(n - 1)
    step = (e - s) / (n - 1)
    x_res[0] = step / 2
    for k in range(1, n - 1, 1):
        x_res[k] = step / 2 + step * k
    return x_res
