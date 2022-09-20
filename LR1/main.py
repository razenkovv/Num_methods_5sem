import numpy as np
from matplotlib import pyplot as plt
import csv

import lagrange_polynomial
import error_compare
import functions

n = 20
s = 0.0
e = 10.0


x_test = np.linspace(s, e, 1000)
y_test = functions.f(x_test)

x_node = np.linspace(s, e, n)
y_node = functions.f(x_node)

x_cheb_node = lagrange_polynomial.create_cheb_nodes(s, e, n)
y_cheb_node = functions.f(x_cheb_node)

x_res = lagrange_polynomial.create_test_x(s, e, n)
y_res = np.zeros(n - 1)
y_cheb_res = np.zeros(n - 1)

for k in range(0, n - 1, 1):
    y_res[k] = lagrange_polynomial.calc(x_res[k], x_node, y_node, n)
    y_cheb_res[k] = lagrange_polynomial.calc(x_res[k], x_cheb_node, y_cheb_node, n)


#print("x_res: ", x_res)
#print("y_res: ", y_res)
#print("y_cheb_res: ", y_cheb_res)
#print("\n")
_error = functions.error(x_res, y_res)
cheb_error = functions.error(x_res, y_cheb_res)
#print("max_error: ", _error)
#print("max_cheb_error: ", cheb_error)
plt.plot(x_test, y_test, c='green', label='function')
#plt.scatter(x_node, y_node, c='blue', s=50, label='nodes')
#plt.scatter(x_cheb_node, y_cheb_node, c='orange', s=50, label='cheb_nodes')
plt.scatter(x_res, y_res, c='red', s=10, label='calc_points')
plt.scatter(x_res, y_cheb_res, c='purple', s=10, label='calc_cheb_points')
plt.annotate("n: %d" % n, xy=(0.6, 0.15), xycoords='axes fraction')
plt.annotate("max_error: %.5f" % _error, xy=(0.6, 0.1), xycoords='axes fraction')
plt.annotate("max_cheb_error: %.5f" % cheb_error, xy=(0.6, 0.05), xycoords='axes fraction')
plt.legend()
plt.show()

# _from = 10
# _to = 200
# _step = 10
# errors, cheb_errors = error_compare.calc_errors(s, e, _from, _to, _step)
# x_i = np.linspace(_from, _to, int((_to - _from) / _step) + 1)
# plt.plot(x_i, errors, label='error')
# plt.plot(x_i, cheb_errors, label='cheb_error')
# plt.legend()
# #plt.show()
# # print("errors: ", errors)
# # print("cheb_errors: ", cheb_errors)
# with open('errors.csv', mode='w', newline='') as error_file:
#     file_writer = csv.writer(error_file, delimiter=',')
#     file_writer.writerow(['n', 'error', 'cheb_error'])
#     for i in range(_from, _to+1, _step):
#         file_writer.writerow([i, errors[int((i - _from) / _step)], cheb_errors[int((i - _from) / _step)]])
