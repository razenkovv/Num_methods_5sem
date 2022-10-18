import numpy as np

import functions


def calc_errors(s, e, _from, _to, _step, func):
    errors = np.zeros(int((_to - _from) / _step) + 1)
    for i in range(_from, _to + 1, _step):
        x_node = np.linspace(s, e, i)
        errors[int((i - _from) / _step)] = functions.error(functions.f_integral(s, e), func(x_node))
        print(i)
    return errors


def generate_x_axis(s, e, _from, _to, _step):
    x_res = np.zeros(int((_to - _from) / _step) + 1)
    for i in range(_from, _to + 1, _step):
        x_res[int((i - _from) / _step)] = ((e - s) / (i - 1))
    return x_res
