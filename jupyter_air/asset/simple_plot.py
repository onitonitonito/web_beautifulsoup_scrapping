"""
# df_plot
"""
print(__doc__)


import numpy as np
import matplotlib.pyplot as plt

# 그래프 함수의 정의


def df_plot(df_series_list,
            figsize=(10, 4),
            xy_start=(0, 0),
            xy_max=(185, 200),
            xy_major=(24, 10),
            xy_minor=(12, 5)):
    """
    # Change grid interval and specify tick labels in Matplotlib
    # https://stackoverflow.com/questions/24943991/change-grid-interval-
    # and-specify-tick-labels-in-matplotlib
    """
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(1, 1, 1)

    # 이곳에 플로트를 추가한다. [ax.plot(df['PM10']), ax.plot(df['PM2.5']),]
    
    titles = ''
    for series in df_series_list:
        ax.plot(series)
        titles += f' {series.name} /'

    # x_max= df.index.size+1 / y_max = np.max(df.PM10)+1
    x_marks_major = np.arange(
        start=xy_start[0],
        stop=xy_max[0],
        step=xy_major[0],
    )

    x_marks_minor = np.arange(
        start=xy_start[0],
        stop=xy_max[0],
        step=xy_minor[0],
    )

    y_marks_major = np.arange(
        start=xy_start[1],
        stop=xy_max[1],
        step=xy_major[1],
    )

    y_marks_minor = np.arange(
        start=xy_start[1],
        stop=xy_max[1],
        step=xy_minor[1],
    )

    ax.set_xticks(x_marks_major)
    ax.set_xticks(x_marks_minor, minor=True)

    ax.set_yticks(y_marks_major)
    ax.set_yticks(y_marks_minor, minor=True)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.4)
    ax.grid(which='major', alpha=0.9)

    ax.legend()
    plt.xlabel('[TIME]')
    plt.title(f'DATA PLOTTING -{titles}')






if __name__ == '__main__':
    pass
