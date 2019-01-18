"""
# get_dataframe from scrapping
#
#
#"""
print(__doc__)

"""
* 청라, 송도지역 미세먼지 측정값 스크래핑
"""
import os
import sys
import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import requests
from bs4 import BeautifulSoup


# get directory information
from config import *


class DataSet(object):
    def __init__(self, url, sensor_type):
        self.url = url
        self.sensor_type = sensor_type
        this_set = self.__class__.__name__
        print(f"New '{this_set}' is created!  ...")


    def get_savelog2(self):
        """
        return 2 types of save log
        save_log  = '20190107_Mon_1800'
        save_log1 = '20190107_1800_Mon'
        """
        now_date = datetime.datetime.strftime(
            datetime.datetime.now(),
            '%Y%m%d_%a_%H00',
        )                               # '20190107_Mon_1800'

        year = now_date[:4]
        month = now_date[4:6]
        day = now_date[6:8]
        week = now_date[9:12]
        hour = now_date[-4:-2]

        save_log = f"{year}{month}{day}_{week}_{hour}00"  # '20190107_Mon_1800'
        save_log1 = f"{year}{month}{day}_{hour}00_{week}"  # '20190107_1800_Mon'
        return (save_log, save_log1)


    def get_BS4_date_data_array(self):
        """ 주의!: 송도와 청라는 데이터 갯수가 틀려서 필터링 방법을 달리해야 함.
        URL = URLS[0]  # 0=청라 - 측정치 1+3 = 4개
        URL = URLS[1]  # 1=송도 - 측정치 1+6 = 7개
        """
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find_all('table', {'class': 'view'})

        tds = table[0].find_all('td')
        fonts = table[0].find_all('font')
        spans = table[0].find_all('span')

        dates = []       # 날짜정보 2개를 담음.
        data = []        # 스크랩핑한 전체 데이터 = 헤드정보 포함

        for n, span in enumerate(spans, 0):
            neat_span = str(span.text).strip()

            """ 날짜와 시간을 분리해서 각각 넣는다 """
            if len(neat_span) > 12:          # 정보 길면, '2018년12월 29일 24시'
                dates.append(neat_span[:-3]) # 날짜 = 2018년 12월 29일 ... 앞쪽
                data.append(neat_span[-3:])  # 시간 = '24시' ... 뒷쪽만 잘라냄
            else:
                data.append(neat_span)       # 그렇지 않으면 그냥 넣는다

        """ 리스트에 담긴 해당 날짜를 보여준다, 그래봤자 2개 지만.. """
        # print(DATE[0]) # 2018년12월 30일 ... 오늘날짜가 먼저 담긴다.
        # print(DATE[1]) # 2018년12월 29일 ... 어제날짜가 다음에 담긴다.
        return dates, data


    def get_columns_units(self, data_array):
        full_columns = ['Time(24Hr)',]
        full_columns.extend(data_array[2:8])
        # ['Time(24Hr)','SO2(ppm)', ... 'CO(ppm)','PM10(㎍/㎥)','PM2.5(㎍/㎥)']

        columns = []       # 컬럼 제목들 만 뽑는다.
        units = []         # 컬럼 단위들 만 뽑는다.

        for item in full_columns:      # full 컬럼값에서 '타이틀'과 '단위'를 분리해 냄
            title = item.split('(')[0]    # Title
            _rest = item.split('(')[1]

            columns.append(title)
            units.append(_rest[:-1])
        return columns, units





    # 그래프 함수의 정의

    def df_plot(self,
                df_series_list,
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


    def df_detail(self,
                    pd_series,
                    color='blue',
                    marker='^',
                    linestyle='--',
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

        plt.plot(pd_series, color=color, marker=marker, linestyle=linestyle)
        plt.yticks(sorted_ytick_label, rotation=0)
        plt.xticks(df.index, df.TIMES, rotation=90)
        plt.title(f'funcname={this_func_name} -- {pd_series.name}')
        plt.legend()
        plt.grid()


    def sm_plot(self, df_column):
        # plt.figure(figsize=(10,4))
        plt.plot(df_column)
        """ 그래프에 텍스트를 입히는 옵션 """
        plt.title("DATA PLOTTING")        # 타이틀
        plt.xlabel('[TIMES]')                      # x 라벨
        plt.ylabel(df_column.name)                   # y 라벨
        plt.legend()
        plt.xticks(df.index, df.TIMES, rotation=90)


    def sm_hist(self, df_column):
        plt.hist(df_column, alpha=0.7)
        """ 그래프에 텍스트를 입히는 옵션 """
        plt.title("DATA HISTOGRAM")        # 타이틀
        plt.xlabel(columns[:1])                      # x 라벨
        plt.ylabel(df_column.name)              # y 라벨


    def sm_scatter(self, df_col1, df_col2):
        plt.scatter(df_col1, df_col2,alpha=0.2)
        """ 그래프에 텍스트를 입히는 옵션 """
        plt.title(
            "SCATTER CHART with {},{}".format(
                df_col1.name,
                df_col2.name,))        # 타이틀
        plt.xlabel(df_col2.name)                     # x 라벨
        plt.ylabel(df_col1.name)    # y 라벨


    def sm_chart2(self, data_series, xlabel):
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




if __name__ == '__main__':
    sd_url = 'https://bit.ly/2EWi9vM'
    cl_url = 'https://bit.ly/2Al7h6y'

    songdo = DataSet(sd_url, 1)
    cheongla = DataSet(cl_url, 1)

    (date, data) = songdo.get_BS4_date_data_array()
    print(date)
    print(data)
