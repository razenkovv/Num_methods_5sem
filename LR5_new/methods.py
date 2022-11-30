import numpy as np


def euler(nodes, init, system):
    res = np.zeros((len(init), len(nodes)))
    res[:, 0] = init
    for i in range(0, len(nodes) - 1):
        h = nodes[i + 1] - nodes[i]
        res[:, [i + 1]] = res[:, [i]] + h * system(res[:, i], nodes[i])
    return res


def runge_kutta_4(nodes, init, system):
    res = np.zeros((len(init), len(nodes)))
    res[:, 0] = init
    for i in range(0, len(nodes) - 1):
        h = nodes[i + 1] - nodes[i]
        k1 = system(res[:, i], nodes[i])
        k2 = system(res[:, [i]] + 0.5 * k1 * h, nodes[i] + 0.5 * h)
        k3 = system(res[:, [i]] + 0.5 * k2 * h, nodes[i] + 0.5 * h)
        k4 = system(res[:, [i]] + k3 * h, nodes[i] + h)
        res[:, [i + 1]] = res[:, [i]] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return res


def adams_3(nodes, init, system):
    res = np.zeros((len(init), len(nodes)))
    res[:, 0:3] = runge_kutta_4(nodes[:3], init, system)
    for i in range(2, len(nodes) - 1):
        h = nodes[i + 1] - nodes[i]
        k1 = system(res[:, i], nodes[i])
        k2 = system(res[:, i - 1], nodes[i - 1])
        k3 = system(res[:, i - 2], nodes[i - 2])
        res[:, [i + 1]] = res[:, [i]] + (h / 12) * (23 * k1 - 16 * k2 + 5 * k3)
    return res
