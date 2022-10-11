import numpy as np
import matplotlib.pyplot as plt
import peakutils as peakutils

import diff
import functions
import error_compare

# print("Enter n: ")
# n = int(input())
n = 10
s = -3.0
e = 3.0

x_test = np.linspace(s, e, 1000)
y_test = functions.f(x_test)

x_node = np.linspace(s, e, n)

y_correct_res = functions.f_diff(x_test)
y_right_res = diff.right_diff(x_node)
y_central_res = diff.central_diff(x_node)

y_correct_res_2 = functions.f_diff_2(x_test)
y_res_2 = diff.second_diff_2(x_node)

# plt.plot(x_test, y_correct_res, c='green', label='correct_diff')
# plt.plot(np.delete(x_node, -1), np.delete(y_right_res, -1), c='red', label='right_diff')

# plt.plot(x_node, y_central_res, c='blue', label='central_diff')
# plt.legend()
# plt.show()

# plt.plot(x_node, y_correct_res_2, c='green', label='correct_diff_2')
# plt.plot(x_node, y_res_2, c='red', label='diff_2')
# plt.show()

_from = 1000
_to = 3000
_step = 10

x_axis = error_compare.generate_x_axis(s, e, _from, _to, _step)

# errors = error_compare.calc_errors(s, e, _from, _to, _step, diff.right_diff, functions.f_diff)
# title = f"First derivative, right differences.\nNumber of nodes: from {_from} to {_to}"

# errors = error_compare.calc_errors(s, e, _from, _to, _step, diff.central_diff, functions.f_diff)
# title = f"First derivative, central differences.\nNumber of nodes: from {_from} to {_to}"

# errors = error_compare.calc_errors(s, e, _from, _to, _step, diff.second_diff_2, functions.f_diff_2)
# # zipped = np.column_stack((x_axis, errors))
# # np.savetxt('errors.csv', zipped)
# # errors = np.loadtxt("errors.csv")[:, 1]
# title = f"Second derivative, central differences, 2nd order.\nNumber of nodes: from {_from} to {_to}"

errors = error_compare.calc_errors(s, e, _from, _to, _step, diff.second_diff_4, functions.f_diff_2)
# zipped = np.column_stack((x_axis, errors))
# np.savetxt('errors_4.csv', zipped)
# errors = np.loadtxt("errors_4.csv")[:, 1]
title = f"Second derivative, central differences, 4th order.\nNumber of nodes: from {_from} to {_to}"

x_plot, y_plot = error_compare.plotting_error_graph(s, e, _from, _to, _step, errors)
mean_tan = np.mean(y_plot / x_plot)

fig = plt.figure(figsize=(8, 8), dpi=200)
fig.suptitle(title, fontsize=15)

plt.subplot(2, 1, 1)
plt.plot(x_plot, y_plot, c='green')
plt.title('Order of approximation')
ax = plt.gca()
ax.set_xlabel("log(h)")
ax.xaxis.set_label_coords(1.04, -0.02)
ax.set_ylabel("log(\u03B4(h)", rotation=0)
ax.yaxis.set_label_coords(-0.02, 1.02)
plt.annotate("mean_tan: %.5f" % mean_tan, xy=(0.7, 0.08), xycoords='axes fraction')

plt.subplot(2, 1, 2)
plt.title('Errors')
ax = plt.gca()
ax.set_xlabel("h")
ax.xaxis.set_label_coords(1.0, -0.02)
ax.set_ylabel("max_error", rotation=0)
ax.yaxis.set_label_coords(-0.07, 1.02)
plt.plot(x_axis, errors)

# indexes1 = peakutils.indexes(errors, thres=0.1e-7)
# indexes2 = peakutils.indexes(-1 * errors, thres=0.1e-7)
# indexes = np.unique(np.concatenate([indexes1, indexes2]))
#
# errors = np.delete(errors, indexes)
# x_axis = np.delete(x_axis, indexes)
# i = np.argmin(errors)
# plt.annotate(f"minimum = {np.min(errors)}\n h = {x_axis[i]}", xy=(0.4, 0.85), xycoords='axes fraction')
plt.show()
#
# print(i)
# print(np.min(errors))
# print(x_axis[i])
#
# plt.plot(x_axis, errors)
# plt.title("Clear data")
# ax = plt.gca()
# ax.set_xlabel("h")
# ax.xaxis.set_label_coords(1.0, -0.02)
# ax.set_ylabel("max_error", rotation=0)
# ax.yaxis.set_label_coords(-0.07, 1.02)
# plt.show()
