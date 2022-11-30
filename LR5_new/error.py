import numpy as np


def correct_func(x):
    return np.sin(x) + x * x


def error(x, y):
    return np.max(np.abs(x - y))


def calc_error_(nodes, init, system, method):
    return error(correct_func(nodes), method(nodes, init, system)[0])


def calc_errors(s, e, init, system, method, _from, _to, _step):
    errors = np.zeros(int((_to - _from) / _step) + 1)
    x_axis = np.zeros_like(errors)
    for i in range(_from, _to + 1, _step):
        nodes = np.linspace(s, e, i)
        errors[int((i - _from) / _step)] = error(correct_func(nodes), method(nodes, init, system)[0])
        x_axis[int((i - _from) / _step)] = nodes[1] - nodes[0]
    return errors, x_axis


def log_errors(s, e, _from, _to, _step, errors):
    x_axis = np.zeros(len(errors))
    err = np.zeros(len(errors))
    for i in range(_from, _to + 1, _step):
        x_axis[int((i - _from) / _step)] = np.log((e - s) / (i - 1))
        err[int((i - _from) / _step)] = np.log(errors[int((i - _from) / _step)])
    return err, x_axis


def runge_error_estimation(nodes, init, system, method, accuracy_order):
    res = method(nodes, init, system)[0]
    if len(nodes) % 2 == 1:
        new_nodes = np.linspace(nodes[0], nodes[-1], int((len(nodes) - 1) / 2 + 1))
    else:
        new_nodes = np.arange(nodes[0], nodes[-1], (nodes[1] - nodes[0]) * 2)
    new_res = method(new_nodes, init, system)[0]
    return np.max(np.abs(res[0::2] - new_res)) / (np.power(2, accuracy_order) - 1)
