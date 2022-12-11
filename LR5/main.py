import numpy as np

import methods
import output
import error

s = 0.0
e = 1.0
init = [0.0, 1.0]


def system(var, x):
    return np.vstack([var[1], 2 - 2 * np.power(x, 3) / np.cos(x) + 2 * x / np.cos(x) * var[0] - np.tan(x) * var[1]])


nodes = np.linspace(s, e, 21)

euler_res = methods.euler(nodes, init, system)[0]
runge_kutta_4_res = methods.runge_kutta_4(nodes, init, system)[0]
adams_3_res = methods.adams_3(nodes, init, system)[0]

output.plot(nodes, euler_res, runge_kutta_4_res, adams_3_res)

_from = 6
_to = 101
_step = 5

euler_error, _x1 = error.calc_errors(s, e, init, system, methods.euler, _from, _to, _step)
runge_error = error.calc_errors(s, e, init, system, methods.runge_kutta_4, _from, _to, _step)[0]
adams_error = error.calc_errors(s, e, init, system, methods.adams_3, _from, _to, _step)[0]

# output.plot_error(_x1, euler_error, runge_error, adams_error)

euler_log_error, _x2 = error.log_errors(s, e, _from, _to, _step, euler_error)
runge_log_error = error.log_errors(s, e, _from, _to, _step, runge_error)[0]
adams_log_error = error.log_errors(s, e, _from, _to, _step, adams_error)[0]

# output.plot_error_log(_x2, euler_log_error, runge_log_error, adams_log_error)

# output.print_error_df(_x1, euler_error, runge_error, adams_error)

print("\nError for h = ", nodes[1] - nodes[0], ":")
print("Runge estimation: ", error.runge_error_estimation(nodes, init, system, methods.runge_kutta_4, 4))
print("Comparing with exact solution: ", error.calc_error_(nodes, init, system, methods.runge_kutta_4))
