import numpy as np
import methods


def correct_func(x):
    return np.sin(x) + x * x


def error(x, y):
    return np.max(np.abs(x - y))


def calc_errors(s, e, p, q, f, lft, rgt, _from, _to, _step, order):
    errors = np.zeros(int((_to - _from) / _step) + 1)
    x_axis = np.zeros_like(errors)
    for i in range(_from, _to + 1, _step):
        nodes = np.linspace(s, e, i)
        left, right = methods.make_system(p, q, f, lft, rgt, nodes, order)
        errors[int((i - _from) / _step)] = error(correct_func(nodes), methods.tdma(left, right))
        x_axis[int((i - _from) / _step)] = nodes[1] - nodes[0]
    return errors, x_axis


def log_errors(s, e, _from, _to, _step, errors):
    x_axis = np.zeros(len(errors))
    err = np.zeros(len(errors))
    for i in range(_from, _to + 1, _step):
        x_axis[int((i - _from) / _step)] = np.log((e - s) / (i - 1))
        err[int((i - _from) / _step)] = np.log(errors[int((i - _from) / _step)])
    return err, x_axis
