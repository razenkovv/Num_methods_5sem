from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

import error


def plot(x_array, euler_res, runge_kutta_4_res, adams_3_res):
    h = x_array[1] - x_array[0]
    fig, ax = plt.subplots(1, 3, figsize=(30, 10))
    ax[0].plot(x_array, euler_res, label='euler', color='red')
    ax[0].scatter(x_array, euler_res, color='red')
    ax[0].set_title(f'Euler method, h={h}')

    ax[1].plot(x_array, runge_kutta_4_res, label='runge_kutta_4', color='red')
    ax[1].scatter(x_array, runge_kutta_4_res, color='red')
    ax[1].set_title(f'Runge_Kutta_4 method, h={h}')

    ax[2].plot(x_array, adams_3_res, label='adams_3', color='red')
    ax[2].scatter(x_array, adams_3_res, color='red')
    ax[2].set_title(f'Adams_3 method, h={h}')

    _x = np.linspace(x_array[0], x_array[-1], int(np.abs(x_array[-1] - x_array[0]) * 1000))
    for ax_ in ax:
        ax_.plot(_x, error.correct_func(_x), label='exact', color='green')
        ax_.legend()
    plt.show()


def plot_error(h_array, euler_error, runge_error, adams_error):
    fig, ax = plt.subplots(1, 3, figsize=(30, 10))
    ax[0].plot(h_array, euler_error, label='euler', color='red')
    ax[0].set_title('Euler error')
    ax[0].set_xlabel('h')
    ax[0].set_ylabel('error')

    ax[1].plot(h_array, runge_error, label='runge_kutta_4', color='red')
    ax[1].set_title('Runge_Kutta_4 error')
    ax[1].set_xlabel('h')
    ax[1].set_ylabel('error')

    ax[2].plot(h_array, adams_error, label='adams_3', color='red')
    ax[2].set_title('Adams_3 error')
    ax[2].set_xlabel('h')
    ax[2].set_ylabel('error')

    plt.show()


def plot_error_log(h_log_array, euler_log_error, runge_log_error, adams_log_error):
    fig, ax = plt.subplots(1, 3, figsize=(30, 10))
    ax[0].plot(h_log_array, euler_log_error, label='euler', color='red')
    ax[0].set_title('Euler error')
    ax[0].set_xlabel('log h')
    ax[0].set_ylabel('log error')
    ax[0].annotate("mean_tan: %.5f" % np.mean(euler_log_error / h_log_array), xy=(0.7, 0.08), xycoords='axes fraction')

    ax[1].plot(h_log_array, runge_log_error, label='runge_kutta_4', color='red')
    ax[1].set_title('Runge_Kutta_4 error')
    ax[1].set_xlabel('log h')
    ax[1].set_ylabel('log error')
    ax[1].annotate("mean_tan: %.5f" % np.mean(runge_log_error / h_log_array), xy=(0.7, 0.08), xycoords='axes fraction')

    ax[2].plot(h_log_array, adams_log_error, label='adams_3', color='red')
    ax[2].set_title('Adams_3 error')
    ax[2].set_xlabel('log h')
    ax[2].set_ylabel('log error')
    ax[2].annotate("mean_tan: %.5f" % np.mean(adams_log_error / h_log_array), xy=(0.7, 0.08), xycoords='axes fraction')

    plt.show()


def print_error_df(h_array, euler_error, runge_error, adams_error, save=-1):
    keys = ['Euler_error', 'Runge_Kutta_4_error', 'Adams_3_error']
    df = pd.DataFrame(index=h_array, columns=keys)
    df.index.name = 'h'
    df.Euler_error = euler_error
    df.Runge_Kutta_4_error = runge_error
    df.Adams_3_error = adams_error
    print(tabulate(df, headers='keys', tablefmt='github'))
    if save == 1:
        df.to_csv('Errors.csv')
