import numpy as np
import functions
import lagrange_polynomial


def calc_errors(s, e, _from, _to, _step):
    errors = np.zeros(int((_to - _from) / _step) + 1)
    cheb_errors = np.zeros(int((_to - _from) / _step) + 1)

    for i in range(_from, _to + 1, _step):
        x_node = np.linspace(s, e, i)
        y_node = functions.f(x_node)

        x_cheb_node = lagrange_polynomial.create_cheb_nodes(s, e, i)
        y_cheb_node = functions.f(x_cheb_node)

        x_res = lagrange_polynomial.create_test_x(s, e, i)
        y_res = np.zeros(i - 1)
        y_cheb_res = np.zeros(i - 1)

        for k in range(0, i - 1, 1):
            y_res[k] = lagrange_polynomial.calc(x_res[k], x_node, y_node, i)
            y_cheb_res[k] = lagrange_polynomial.calc(x_res[k], x_cheb_node, y_cheb_node, i)

        errors[int((i - _from) / _step)] = functions.error(x_res, y_res)
        cheb_errors[int((i - _from) / _step)] = functions.error(x_res, y_cheb_res)

    return errors, cheb_errors
