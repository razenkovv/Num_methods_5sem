import numpy as np
from matplotlib import pyplot as plt

import diff
import functions
import error_compare


#print("Enter n: ")
#n = int(input())
n = 100
s = -3.0
e = 3.0

x_test = np.linspace(s, e, 1000)
y_test = functions.f(x_test)

x_node = np.linspace(s, e, n)

y_correct_res = functions.f_diff(x_node)
y_right_res = diff.right_diff(x_node)
y_central_res = diff.central_diff(x_node)

y_correct_res_2 = functions.f_diff_2(x_node)
y_res_2 = diff.second_diff_2(x_node)

# plt.plot(x_node, y_correct_res, c='green', label='correct_diff')
# plt.plot(x_node, y_right_res, c='red', label='right_diff')
# plt.plot(x_node, y_central_res, c='blue', label='central_diff')
#
# plt.plot(x_node, y_correct_res_2, c='green', label='correct_diff_2')
# plt.plot(x_node, y_res_2, c='red', label='diff_2')

_from = 10
_to = 1000
_step = 1
errors = error_compare.calc_errors(s, e, _from, _to, _step, diff.second_diff_2, functions.f_diff_2)
print(errors, "\n\n\n")
x_plot, y_plot = error_compare.plotting_error_graph(s, e, _from, _to, _step, errors)
print(x_plot, y_plot)
plt.plot(x_plot, y_plot, c='green', label='log(d_h) ~ log(h)')
plt.legend()
plt.show()
