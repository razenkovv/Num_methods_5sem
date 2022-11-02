import numpy as np

import functions


def calc_errors(s, e, _from, _to, _step, func):
    errors = np.zeros(int((_to - _from) / _step) + 1)
    for i in range(_from, _to + 1, _step):
        x_node = np.linspace(s, e, i)
        errors[int((i - _from) / _step)] = functions.error(functions.f_integral(s, e), func(x_node))
        print(i)
    return errors


def calc_upper_bound_errors(s, e, _from, _to, _step, func):
    errors = np.zeros(int((_to - _from) / _step) + 1)
    for i in range(_from, _to + 1, _step):
        x_node = np.linspace(s, e, i)
        h = x_node[1] - x_node[0]
        m = np.max(functions.f_diff(x_node))
        errors[int((i - _from) / _step)] = 0.5 * np.power(h, 2) * m * (i - 1)
        print(i)
    return errors


def generate_x_axis(s, e, _from, _to, _step):
    x_res = np.zeros(int((_to - _from) / _step) + 1)
    for i in range(_from, _to + 1, _step):
        x_res[int((i - _from) / _step)] = ((e - s) / (i - 1))
    return x_res


def plotting_error_graph(s, e, _from, _to, _step, errors):
    x_res = np.zeros(int((_to - _from) / _step) + 1)
    y_res = np.zeros(int((_to - _from) / _step) + 1)
    for i in range(_from, _to + 1, _step):
        x_res[int((i - _from) / _step)] = (np.log((e - s) / (i - 1)))
        y_res[int((i - _from) / _step)] = (np.log(errors[int((i - _from) / _step)]))
    return x_res, y_res
