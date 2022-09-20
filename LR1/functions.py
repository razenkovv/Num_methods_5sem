import numpy as np


def f(arg):
    return np.sin(np.power(np.exp(1), (arg / 3)) / 10)


def error(x, y):
    _max = 0
    for _x, _y in zip(x, y):
        diff = abs(_y - f(_x))
        if diff > _max:
            _max = diff
    return _max
