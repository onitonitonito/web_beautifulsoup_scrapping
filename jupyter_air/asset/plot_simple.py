import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 그래프 함수의 정의


def df_plot(df_column):
    # plt.figure(figsize=(10,4))
    plt.plot(df_column)
    """ 그래프에 텍스트를 입히는 옵션 """
    plt.title("DATA PLOTTING")        # 타이틀
    plt.xlabel(COLUMNS[:1])                      # x 라벨
    plt.ylabel(df_column.name)                   # y 라벨
    plt.legend()
    plt.xticks(df.index, df.TIMES, rotation=90)


def df_hist(df_column):
    plt.hist(df_column)
    """ 그래프에 텍스트를 입히는 옵션 """
    plt.title("DATA HISTOGRAM")        # 타이틀
    plt.xlabel(COLUMNS[:1])                      # x 라벨
    plt.ylabel(df_column.name)                   # y 라벨


def df_scatter(df_col1, df_col2):
    plt.scatter(df_col1, df_col2, alpha=0.2)
    """ 그래프에 텍스트를 입히는 옵션 """
    plt.title(
        "SCATTER CHART with {},{}".format(
            df_col1.name,
            df_col2.name,))        # 타이틀
    plt.xlabel(df_col2.name)                     # x 라벨
    plt.ylabel(df_col1.name)                     # y 라벨


def plot_2charts(data_series, xlabel):
    """
    # 히스토그램 + 박스플롯을 4x4화면 윗쪽 2개로 플롯해줍니다.
    """
    plt.figure()
    plt.subplot(221)
    plt.hist(data_series)
    plt.xlabel(xlabel)

    plt.subplot(222)
    sns.boxplot(data_series)
    plt.show()






def plot_detail(pd_series,
                color='blue', marker='^', linestyle='--',
                xtick_interval=2,
                ytick_interval=5,):
    """
    style = color='blue', marker='^', linestyle='--'   ... default style
    linestyle = '-', '--', '-.', ':', '', (offset, on-off-seq), ...
    marker_style = '.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4',
                    's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_',
    xtick_interval = 2, ytick_interval = 5
    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html?highlight=plot%20color
    """
    this_func_name = sys._getframe().f_code.co_name
    ytick_start = pd_series.min() - (pd_series.min() % ytick_interval)
    ytick_end = pd_series.max() - (pd_series.max() % ytick_interval) + ytick_interval

    sorted_ytick_label = sorted([
        *np.arange(ytick_start, ytick_end, ytick_interval).tolist(),
        pd_series.min(),
        pd_series.max(),
        pd_series.mean(),
        pd_series.median()])

    plt.figure(figsize=(10, 4))

    plt.plot(pd_series, color=color, marker=marker, linestyle=linestyle)
    plt.yticks(sorted_ytick_label, rotation=0)
    # plt.xticks(df.index, df.TIMES, rotation=90)
    plt.title(f'funcname={this_func_name} -- {pd_series.name}')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    from random import randint

    df_array = {
        "A": [ randint(0,100) for i in range(50)],
        "B": [ randint(0,100) for i in range(50)],
        "C": [ randint(0,100) for i in range(50)],
    }

    df1 = pd.DataFrame(df_array)

    # print(df1)
    #   A	B	C
    # 0	foo	0	A
    # 1	foo	1	A
    # 2	foo	1	B
    # 3	bar	1	A
    # 4 foo 0   A

    plot_detail(df1.A)
    plot_detail(df1.B)
    plot_detail(df1.C)
