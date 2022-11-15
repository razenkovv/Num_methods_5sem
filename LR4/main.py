import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tabulate import tabulate

import functions
import methods

s = 0.0
e = 10.0

precisions = np.logspace(-1, -12, num=12, endpoint=True, base=10.0)
keys = ["Bisection_solution", "B_Number_of_iterations", "Newton_solution", "N_Number_of_iterations"]
df = pd.DataFrame(index=precisions, columns=keys)

for precision in precisions:
    df.loc[precision] = methods.bisection(functions.f, s, e, precision) + \
                        methods.newton(functions.f, functions.diff_f, s, e, (s+e)/2, precision)

print(tabulate(df, headers='keys', tablefmt='github', floatfmt=['.0e', '.15f', '.f', '.15f', '.f']))


methods.anim_func(functions.f, functions.diff_f, s, e, (s+e)/2, 1e-3, pause=1)
