from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate

import error


def plot(x_array, res1, res2):
    h = x_array[1] - x_array[0]
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    ax[0].plot(x_array, res1, label='calc', color='red')
    ax[0].scatter(x_array, res1, color='red')
    ax[0].set_title(f'1st order, h={h}')

    ax[1].plot(x_array, res2, label='calc', color='red')
    ax[1].scatter(x_array, res2, color='red')
    ax[1].set_title(f'2nd order, h={h}')

    _x = np.linspace(x_array[0], x_array[-1], int(np.abs(x_array[-1] - x_array[0]) * 1000))
    for ax_ in ax:
        ax_.plot(_x, error.correct_func(_x), label='exact', color='green')
        ax_.legend()
    plt.show()


def plot_error(h_array, error1, error2):
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    ax[0].plot(h_array, error1, color='red')
    ax[0].set_title('1st order error')
    ax[0].set_xlabel('h')
    ax[0].set_ylabel('error')

    ax[1].plot(h_array, error2, color='red')
    ax[1].set_title('2nd order error')
    ax[1].set_xlabel('h')
    ax[1].set_ylabel('error')

    plt.show()


def plot_error_log(h_log_array, log_error1, log_error2):
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    ax[0].plot(h_log_array, log_error1, color='red')
    ax[0].set_title('1st order error')
    ax[0].set_xlabel('log h')
    ax[0].set_ylabel('log error')
    ax[0].annotate("mean_tan: %.5f" % np.mean(log_error1 / h_log_array), xy=(0.7, 0.08), xycoords='axes fraction')

    ax[1].plot(h_log_array, log_error2, label='runge_kutta_4', color='red')
    ax[1].set_title('2nd order error')
    ax[1].set_xlabel('log h')
    ax[1].set_ylabel('log error')
    ax[1].annotate("mean_tan: %.5f" % np.mean(log_error2 / h_log_array), xy=(0.7, 0.08), xycoords='axes fraction')

    plt.show()


def print_error_df(h_array, error1, error2, save=-1):
    keys = ['1st_order_error', '2nd_order_error']
    df = pd.DataFrame(index=h_array, columns=keys)
    df.index.name = 'h'
    df['1st_order_error'] = error1
    df['2nd_order_error'] = error2
    print(tabulate(df, headers='keys', tablefmt='github'))
    if save == 1:
        df.to_csv('Errors.csv')
