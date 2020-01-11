"""
# app.py - (Temporary) PyAutoGui제어
"""
# https://www.pygame.org/wiki/SettingWindowPosition
# pag.moveTo(x=1877, y=1060)    # check!... (1st) 캘린더
# pag.moveTo(x=20, y=1060)      # check!... (1st) 윈도우 시작
# pag.moveTo(x=2490, y=15)      # check!... (2nd) CMD 85x80 @(0,0) [x]
# pag.moveTo(x=1895, y=20)      # check!... (1st) pygame 300x100 @(1620,40) [x]


import os
import sys
import pygame
import pyautogui as pag

from pygame.locals import *
from config_autogui import *
from datetime import datetime as dd

os.environ['SDL_VIDEO_WINDOW_POS'] = "1620,40" # window starts posXY[nw]

print(__doc__)

def main():
    """입력받기: 1=좌표체크(with 'SPACE') / ENTER=타이머 설정! """
    global ttime_fire, ttime_prep, target_time
    global ttime_h, ttime_m, ttime_s, ttime_f

    if input("*** SELECT: [1]=좌표체크! / [ENTER]=타이머 설정!").startswith("1"):
        set_basic_screen((300,100),"TAP HERE!")
        display_message(text="TAP=SPACE!",
                        font_color=RED,
                        size=45, posxy=(10,30),
                        )
        pygame.display.update()

        print(f"* SCREEN_SIZE  : {pag.size()}") # Size(width=1920, height=1080)
        while 1:
            check_pointer_xy_coords()           # 스페이스바로 좌표체크

    else:
        time_input = f"\n\n 타겟시간입력: (예)'{str(dd.now())[-16:-7]}'   : "
        ttime_fire = input(time_input)     # 이벤트 클릭 시간!
        ttime_prep = get_prep_time(str_time_fire=ttime_fire, minute_before=1)

        print(f"* CURRENT TIME : {dd.now()}")
        print(f"* PREPERATION_TIME        = {ttime_prep} ")
        print(f"* ACTIVATE_TIME_TRIGGER   = {ttime_fire} ***", "\n\n")

        set_basic_screen((300,100),"SET O.K!")
        display_message(text=f"*{ttime_prep} - [PREP] ",
                        font_color=GREEN,
                        size=25, posxy=(10,25),
                        )
        display_message(text=f"*{ttime_fire} - [BANG] ***",
                        font_color=MAGENTA,
                        size=25, posxy=(10,57),
                        )
        pygame.display.update()

        while 1:
            """ 랙 때문에 어려움이 있다."""
            limit_time = 1000
            trigger = False

            while 1:
                time_now = dd.now()
                target_time = time_now.strftime("%H:%M:%S")

                ttime_h = target_time[-8:-6]
                ttime_m = target_time[-5:-3]
                ttime_s = target_time[-2:]
                ttime_f = time_now.strftime("%f")

                if (trigger == False) and int(ttime_f) < limit_time:
                    is_trigger_time()
                    trigger = True

                if ttime_f != dd.now().strftime("%f"):
                    trigger=False

def event_prep(choose=1):
    """ default = 1, 캘린더를 띄운다
    # pag.click(x=1877, y=1060, clicks=1)    # (1st) 캘린더
    # pag.click(x=20, y=1060, clicks=1)      # (1st) 윈도우 시작
    # pag.click(x=2490, y=15, clicks=1)      # (2nd) CMD 85x80 @(0,0) [x]
    # pag.click(x=1895, y=20, clicks=1)      # (1st) pygame 300x100 [x]
    """
    xy_coords = {
        '1'  : (1877 , 1060, 'calendar'),
        '2'  : (20   , 1060, 'start'   ),
        '3'  : (2049 ,   15, 'cmd'     ),
        '4'  : (1895 ,   20, 'pygame'  ),
        'bang':(3739 , 1115, 'bang_xy'  ),
        'move':(2980 ,  330, 'center_xy'),
    }

    pag.click(xy_coords[str(choose)][0], xy_coords[str(choose)][1], clicks=1)
    pag.moveTo(xy_coords['move'][0], xy_coords['move'][1])   # (2nd)에서 대기

def event_bang():
    """
    # pag.click(x=3739, y=1115, clicks=3)   # (2nd) 의견추가버튼
    # pag.click(clicks=3, duration=0)       # (2nd) 확인버튼 - 1차
    # pag.doubleClick()                     # (2nd) 확인버튼 - 2차(랙대비)

    """
    # 메인 트리거 이벤트 - HERE!
    pag.click(x=3739, y=1115, clicks=1, duration=0.0)

    pag.click(clicks=1, duration=0)
    pag.click(clicks=1, duration=0)
    pag.click(clicks=1, duration=0)
    # pag.doubleClick()
    pass

def decorate_after_bang():
    # 나머지는 쓸데없는 데코레이션 이벤트
    print()
    print("---"*4, f"{ttime_s}.{ttime_f} [BANG] ***", flush=True)
    print("\n")
    [print("RANG--rang--RANG---rang!!", flush=True) for i in range(3)]

    print()
    print(dd.now())
    sys.exit()

def is_trigger_time():
    """매초 00, 타임스탬프를 찍고, sec='00' 일때 클릭 이벤트를 실행"""
    if ttime_s == '00':
        if target_time == ttime_fire:
            event_bang()
            decorate_after_bang()

        elif target_time == ttime_prep:
            event_prep()
            print("---"*4, f"{ttime_s}.{ttime_f} [PREP]▶", flush=True)

        else:
            print("---"*4, f"{ttime_s}.{ttime_f}", flush=True)
    else:
        print(f"{target_time}.{ttime_f}", flush=True)

def check_pointer_xy_coords():
    """이벤트 키값에 대응하는 event_dict로 키 이벤트 입력 판단"""
    for event in pygame.event.get():
        event_dict = {
            'space': [(event.type == KEYDOWN and event.key == K_SPACE), ],
            'quit' : [(event.type == QUIT),
                     (event.type == KEYDOWN and event.key == K_ESCAPE), ],
        }

        # show key-event on console
        """# IF - Keybinding State = keydown-stroke"""
        for key in event_dict.keys():

            if True in [*event_dict[key]]:    # 키-이벤트가 발생판단
                # print(f'----[{key.upper()}]----')  # for TEST

                if key == 'quit':
                    pygame.quit()
                    sys.exit()
                    break

                if key == 'space':
                    text_pos = str(pag.position())
                    print(text_pos)
                    DISPLAYSURF.fill(YELLOW)
                    display_message(text_pos, size=25, posxy=(10,40), font_color=(52, 63, 179))
                    pygame.display.update()

def set_basic_screen(screen_size, caption="CAPTION HERE"):
    """set default window screen"""
    global DISPLAYSURF
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode(screen_size)
    DISPLAYSURF.fill(YELLOW)
    pygame.display.set_caption(caption)

def display_message(text, size, posxy, font_color, delay_time=0):
    """HELPER(): for display_*() """
    global DISPLAYSURF
    textfont = pygame.font.Font("freesansbold.ttf", size)
    text = textfont.render(text, True, font_color)
    DISPLAYSURF.blit(text, posxy)



if __name__ == '__main__':
    main()
