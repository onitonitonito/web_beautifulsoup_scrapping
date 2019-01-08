"""-------------------------
#
#
#
#"""
print(__doc__)

import os

dir_work = os.getcwd()

# data 자동저장 폴더
dir_data = os.path.join(dir_work, *['static', 'data',])
dir_data_collect = os.path.join(dir_work, *['static', 'data', 'collect',])
dir_data_trash   = os.path.join(dir_work, *['static', 'data', 'trash',])

# 이미지 결과 자동저장 폴더
dir_img = os.path.join(dir_work, *['static', 'img',])
dir_img_heatmap = os.path.join(dir_work, *['static', 'img', 'heatmap',])
dir_img_nulschool = os.path.join(dir_work, *['static', 'img', 'nulschool',])
dir_img_plot_plot = os.path.join(dir_work, *['static', 'img', 'plot_plot',])
dir_img_plot_scatter = os.path.join(dir_work, *['static', 'img', 'plot_scatter',])
dir_img_test = os.path.join(dir_work, *['static', 'img', 'test',])



if __name__ == '__main__':
    [print(_dir) for _dir in [
        dir_work,
        dir_data,
        dir_data_collect,
        dir_data_trash,
        dir_img,
        dir_img_heatmap,
        dir_img_nulschool,
        dir_img_plot_plot,
        dir_img_plot_scatter,
        dir_img_test,
    ]]
