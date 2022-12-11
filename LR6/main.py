import numpy as np

import error
import methods
import output

# u" + p(x)u' + q(x)u = f(x)
# lft[0] * u'(s) + lft[1] * u(s) = lft[2]
# rgt[0] * u'(e) + rgt[1] * u(e) = rgt[2]

lft = [-1, 2, -1]
rgt = [1, 3, 8.0647]

s = 0.0
e = 1.0
n = 21  # h = 0.05 for n = 21

nodes = np.linspace(s, e, n)


def p(x): return np.tan(x)
def q(x): return -2 * x / np.cos(x)
def f(x): return 2 - 2 * x ** 3 / np.cos(x)


left1, right1 = methods.make_system(p, q, f, lft, rgt, nodes, order=1)
left2, right2 = methods.make_system(p, q, f, lft, rgt, nodes, order=2)
res1 = methods.tdma(left1, right1)
res2 = methods.tdma(left2, right2)

# output.plot(nodes, res1, res2)

_from = 6
_to = 101
_step = 5

error1, _x1 = error.calc_errors(s, e, p, q, f, lft, rgt, _from, _to, _step, order=1)
error2 = error.calc_errors(s, e, p, q, f, lft, rgt, _from, _to, _step, order=2)[0]

# output.plot_error(_x1, error1, error2)

log_error1, _x2 = error.log_errors(s, e, _from, _to, _step, error1)
log_error2 = error.log_errors(s, e, _from, _to, _step, error2)[0]

# output.plot_error_log(_x2, log_error1, log_error2)

output.print_error_df(_x1, error1, error2)
