"""
# functions_class.py - function & class definition
"""
# apply: multi_pop_tabs / stock_weekly_chart.ipynb
print(__doc__)

import random
import matplotlib

import matplotlib.pyplot as plt

from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

matplotlib.use('Qt5Agg')

class ScrollWindow(QtWidgets.QMainWindow):
    """ Pyplot 스크롤바 만들어주는 클래스 : 사용 a = ScrollWindow(fig)"""
    def __init__(self, fig):
        self.qapp = QtWidgets.QApplication([])

        QtWidgets.QMainWindow.__init__(self)
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        self.widget.setLayout(QtWidgets.QVBoxLayout())
        self.widget.layout().setContentsMargins(0,0,0,0)
        self.widget.layout().setSpacing(0)

        self.fig = fig
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        self.scroll = QtWidgets.QScrollArea(self.widget)
        self.scroll.setWidget(self.canvas)

        self.nav = NavigationToolbar(self.canvas, self.widget)
        self.widget.layout().addWidget(self.nav)
        self.widget.layout().addWidget(self.scroll)

        self.show()
        exit(self.qapp.exec_())

def set_font_hanguel_graph():
    """맷플롯 그래프에서 한글 깨짐 방지"""
    from matplotlib import font_manager, rc
    dir_font = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=dir_font).get_name()
    rc('font', family=font_name)
    print(f"*** Hanguel font for pyplot graph is set! ... '{dir_font}'***")

def get_today_header():
    """
    # get save filename header from datatime like below,
    #   - '2019Nov14(Thu)AM0118'    ... '%Y%h%d(%a)%p%I%M'
    #   - '14Nov(Thu)AM0118_2019'   ... '%d%h(%a)%p%I%M_%Y'
    """
    import datetime
    time_now = datetime.datetime.now()
    time_format = '%d%h(%a)%p%I%M_%Y'
    header = datetime.datetime.strftime(time_now, time_format)
    print(f"Today is ... {header}")
    return header

def get_markdown_echo(code_stock, name, target, detail=True):
    url = "https://ssl.pstatic.net/imgfinance/chart/item/area/"
    sidecode=random.random()

    if detail:
        echo = f"""
## {name} ({code_stock[name]})
- URL = {url}
- target={target}
- png?sidedode = {sidecode}
![__CHART__]({url}/{target}/{code_stock[name]}.png?sidcode={sidecode})
"""
    else:
        echo = f"""
- target={target}
![__CHART__]({url}/{target}/{code_stock[name]}.png?sidcode={sidecode})
"""
    return echo
