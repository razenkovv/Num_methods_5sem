import numpy as np
from matplotlib import pyplot as plt

import error_compare
import functions
import integrate

n = 10000
s = 0.0
e = 5.0

# x_node = np.linspace(s, e, n)
# correct_result = functions.f_integral(s, e)
# num_res = integrate.simpson_method(x_node)
# print("Calculated res: ", num_res)
# print("Correct result: ", correct_result)
# print("Error: ", np.abs(num_res - correct_result))


_from = 101
_to = 1001
_step = 2

x_axis = error_compare.generate_x_axis(s, e, _from, _to, _step)

# errors = error_compare.calc_errors(s, e, _from, _to, _step, integrate.rectangle_method)
# title = f"Rectangle method. Number of nodes: from {_from} to {_to}"
# print(errors)

# errors = error_compare.calc_errors(s, e, _from, _to, _step, integrate.trapz_method)
# title = f"Trapz method.\nNumber of nodes: from {_from} to {_to}"
# print(errors)

# errors = error_compare.calc_errors(s, e, _from, _to, _step, integrate.simpson_method)
# title = f"Simpson method.\nNumber of nodes: from {_from} to {_to}"
# print(errors)

# plt.title(title)
# ax = plt.gca()
# ax.set_xlabel("h")
# ax.xaxis.set_label_coords(1.0, -0.02)
# ax.set_ylabel("error", rotation=0)
# ax.yaxis.set_label_coords(-0.07, 1.02)
# plt.plot(x_axis, errors)
# plt.show()

errors1 = error_compare.calc_errors(s, e, _from, _to, _step, integrate.rectangle_method)
errors2 = error_compare.calc_errors(s, e, _from, _to, _step, integrate.trapz_method)
errors3 = error_compare.calc_errors(s, e, _from, _to, _step, integrate.simpson_method)
zipped = np.column_stack((x_axis, errors1, errors2, errors3))
np.savetxt('errors.csv', zipped, delimiter=',', header="h,rectangle,trapz,simpson")
