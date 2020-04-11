"""
# practice.py - PyAutoGui제어 - 키보드/마우스 제어페키지
"""
# https://gosmcom.tistory.com/104

import time
import skimage.io
import numpy as np
import matplotlib.pyplot as plt
import pyautogui as pag

from PIL import Image, ImageOps
from config_autogui import *

def run01():
    # 현재 화면사이즈 확인 ... Size(width=1920, height=1080)
    print(pag.size())

    # 화면 좌표는 실행하는 기기에 따라 다르다 ... 체크/변경 필요
    # pag.moveTo(x=2809, y=-100)
    # pag.click(clicks=1)

    echoes = [
        [f"'''\n", 0.0],
        [f"Hello World!\n", 0.0],
        [f"Hello World!\n", 0.15],
        [f"Hello World!\n", 0.3],
        [f"'''\n\n", 0.0],
    ]

    # 타이핑함수
    time.sleep(1)
    # pag.typewrite("\n\n'''Hello World\n")
    # pag.typewrite("Hello World'''\n", interval=0.15)
    [pag.typewrite(*item) for item in echoes]

    # 마우스이동
    pag.moveTo(x=100, y=100, duration=3.0)

def run03():
    """
    >>> from PIL import Image
    >>> img = Image.fromarray(np.ones((100, 100, 3), dtype=np.uint8))  # RGB image
    >>> ImageOps.invert(img)
    """
    name_img = dir_home_images + 'banana.png'
    img = Image.fromarray(skimage.io.imread(fname=name_img))  # RGB image
    ImageOps.invert(img)
    plt.imshow(img)
    plt.show()


def run02():
    print('*** Start to find! ***')
    name_img = dir_home_images + 'banana.png'
    img_array = skimage.io.imread(fname=name_img)
    print(img_array.shape)           # (173, 248, 3)
    plt.imshow(img_array)
    plt.show()

    # 이미지 중앙좌표 찾기, confidence: 정확도
    # pos = pag.locateCenterOnScreen('banana.png', confidence=0.8)
    img_PIL = Image.fromarray(img_array)  # RGB image
    ImageOps.invert(img_PIL)

    # pos = pag.locateCenterOnScreen(image=img_array) # no attribute 'mode'
    pos = pag.locateCenterOnScreen(image=img_PIL)
    print(type(pos)); quit()

    print('중앙좌표:', pos)
    pag.moveTo(pos[0], pos[1])  # 이미지 중앙(center) 포인터 이동
    time.sleep(2)

    # 이미지 왼쪽, 위, 가로,세로길이 좌표찾기, confidence : 정확도
    pos = pag.locateOnScreen(name_img)
    print('박스모델 좌표:', pos)
    pag.moveTo(pos[0], pos[1])  # 이미지 좌상(NW) 포인터 이동


def get_posXY():
    # 현재 마우스 좌표확인
    return pag.position()


if __name__ == '__main__':
    # run01()
    run02()
    # run03()

    # print(get_posXY())              # Point(x=3146, y=287)
