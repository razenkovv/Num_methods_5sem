import numpy as np
from matplotlib import pyplot as plt


def bisection(f, s, e, eps):
    counter = 1
    while e - s > eps:
        counter += 1
        c = (s + e)/2
        if f(s)*f(c) > 0:
            s = c
        else:
            e = c
    return [(e+s)/2, counter]


def newton(f, diff_f, s, e, c, eps):
    c_n = c - f(c)/diff_f(c)
    counter = 1
    while np.abs(c_n - c) > eps:
        counter += 1
        c = c_n
        c_n = c_n - f(c_n) / diff_f(c_n)
    return [c_n, counter]


def plotting(counter, pause, fig, ax, c, f, diff_f):
    x = np.linspace(0, 20, 1000)
    ax.set_xlim(0, 20)
    ax.set_ylim(-0.5, 2.5)
    ax.set_title('Iteration: ' + str(counter))
    ax.plot(x, np.zeros(x.shape), color='black')
    ax.plot(x, diff_f(c) * (x - c) + f(c))
    ax.plot(x, f(x))
    ax.scatter(8.143, 0, linewidth=3, color='black')
    ax.scatter(10.915, 0, linewidth=3, color='black')
    ax.scatter(c - f(c)/diff_f(c), 0, linewidth=1.5, color='red')
    plt.show()
    plt.pause(pause)
    plt.cla()


def anim_func(f, diff_f, s, e, c, eps, pause):
    counter = 1
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    plt.ion()
    c_n = c - f(c)/diff_f(c)
    while np.abs(c_n - c) > eps:
        plotting(counter=counter, pause=pause, fig=fig, ax=ax, c=c, f=f, diff_f=diff_f)
        counter += 1
        c = c_n
        c_n = c_n - f(c_n) / diff_f(c_n)
    plt.ioff()
    return c_n
