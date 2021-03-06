"""
# stock_charts_view / pstaticNet - jupyter notebook conversion
# config_stocks.py 에서 변수를 가져옴 (종목명/코드)
"""
# ing = 테스트중인 FILE!
print(__doc__)

import os
import numpy as np
import skimage.io
import matplotlib.pyplot as plt

import assets.script_run
from assets.functions_class import (
                            get_today_header,
                            set_font_hanguel_graph
                        )
from assets.config_stocks import (
                            URL,
                            targets,
                            dir_works,

                            show_dict,
                            show_names_codes,

                            get_sidecode,
                            get_names_codes_partial,
                        )

set_font_hanguel_graph()        # pyplot 그래프 상, 한글폰트 깨짐 방지

HEADER = get_today_header()     # 05Dec(Thu)AM0803_2018

DIRS_INTERESTS = [filename
            for filename in os.listdir(dir_works)
            if not '.' in filename]

CODES = [dir.split('_')[-1]
            for dir in DIRS_INTERESTS]


def main():
    """ 6개 ~ 최대12개 챠트만 나열해서 봅니다. 그게 제일, 보기 적당 해"""

    # 기존 폴더에 있는 png 화일을 모두 지운다.
    for dir in DIRS_INTERESTS:
        dir_target = dir_works + dir + '\\'
        remove_file_of_ext(dir_target, 'png', echo=1)

    # 확인 할 종목명, 코드를 보여준다.
    show_dict()

    # only save all = True / just watch = Flase
    is_save = is_save_answer()

    # show_names_codes(index_partial) --> global
    index_partial = get_index_partial()

    save_or_show(index_partial, is_save)

def get_index_partial():
    """ index_partial 을 input 입력 받는다. """
    print()
    answer = input(
                "idx_array를 ','구분 4개 이상 입력 짝수로 입력 (예) 4,3,1,2\n" +
                "or [ENTER]=Autonomous select by dir_name!\n :    "
                ).strip()
    if answer[0:1].isnumeric():
        print([int(idx)-1 for idx in answer.split(",")])
        return [int(idx)-1 for idx in answer.split(",")]
    else:
        print([idx for idx in range(4)])
        return [idx for idx in range(4)]

def is_save_answer():
    """ to ask save and return True/False as answer """
    question = "\n*** ONLY Save all the targeted charts? [Yes=1 / No=Enter]"
    answer = True if input(question).startswith('1') else False
    print(f"(Save all the charts? = '{answer}')")
    return answer

def get_images_nparray(target, index_partial):
    """
    # HELPER() for show_charts_axes() :목적챠트(target)에 대해
    # index_partial 범위 skimage obj. array 반납
    """
    _, codes_partial = get_names_codes_partial(index_partial)

    images_nparray = []
    for code in codes_partial:
        img_url = f"{URL}/{target}/{code}.png?sidcode={get_sidecode(13)}"
        im_array = skimage.io.imread(img_url)
        images_nparray.append(im_array)
    return images_nparray

def show_charts_axes(target, index_partial):
    """ 헬퍼함수를 사용해서 target 과 index_partial 받아서 챠트 출력. """
    images_nparray = get_images_nparray(target, index_partial)
    (names_partial, codes_partial) = get_names_codes_partial(index_partial)

    (cols, rows) = (2, int(len(names_partial)/2))     # (2 , 6)
    fig, ax = plt.subplots(ncols=cols, nrows=rows, figsize=(18, rows*6))

    i = 0
    for row in range(rows):
        for col in range(cols):
            # TODO: Something might wrong! within 2~3, or odd number!
            try:
                # print(row,col)   # ... for test
                ax[row,col].imshow(images_nparray[i])
                ax[row,col].set_title(
                    f"{names_partial[i]} ({codes_partial[i]}) by {target}"
                    )
            except:
                print("*** TODO: Error! HOTFIX! ***")
                pass
            i += 1
    plt.tight_layout(pad=0.1)

def save_or_show(index_partial, is_save=False):
    """
    HELPER() for main() : 저장만 하든지, 보기 만 하든지
    # save_or_show(index_partial, is_save=False)
    # index_partial =
    # targets = [day, week, ...] / HEADER = date_prefix
    """
    global targets, HEADER

    index_partial_np = np.array(index_partial)
    count_np_dimension = len(index_partial_np.shape)

    # # FOR TEST
    # print(index_partial_np.shape)
    # print(len(index_partial_np.shape)); quit()

    if count_np_dimension == 1:

        print("*** LIST IS SINGLE-DIMENSIONAL!. RUN ... ({i})!")
        for i, target in enumerate(targets):
            proceed = f"{i+1}/{len(targets)}"  # 진행정도 표시
            question = f"\n\nDraw '{target}'graph({proceed})? ... [OK=Ent./NO=1]"

            # save all charts designated, properly 4 charts
            if is_save:
                print(f"\n... '{i:02}.{target}' chart is saved", flush=True)
                show_charts_axes(target, index_partial)
                plt.savefig(fname=dir_works + f"{HEADER}_{i:02}_{target}.png")

            # just show images for each target charts
            else:
                if not input(question).startswith("1"):
                    show_charts_axes(target, index_partial)
                    plt.show()
                else:
                    print(f" *** '{target}' charts are skipped! ***")

    else:
        for i in range(count_np_dimension):
            index_partial = index_partial_np[i]
            print("*** LIST IS MULTI-DIMENSIONAL!. RUN ... ({i})!")

            for i, target in enumerate(targets):
                proceed = f"{i+1}/{len(targets)}"  # 진행정도 표시
                question = f"\n\nDraw '{target}'graph({proceed})? ... [OK=Ent./NO=1]"

                # save all charts designated, properly 4 charts
                if is_save:
                    print(f"\n... '{i:02}.{target}' chart is saved", flush=True)
                    show_charts_axes(target, index_partial)
                    plt.savefig(fname=dir_works + f"{HEADER}_{i:02}_{target}.png")

                # just show images for each target charts
                else:
                    if not input(question).startswith("1"):
                        show_charts_axes(target, index_partial)
                        plt.show()
                    else:
                        print(f" *** '{target}' charts are skipped! ***")


def remove_file_of_ext(dir_target, ext, echo=False):
    """ remove all the *.ext in the dir_target """
    dir_current = dir_target.partition('works')[-1]
    exts = [file
                for file in  os.listdir(dir_target)
                if file.endswith(f".{ext}")
           ]
    print(f"\nSCAN DIR in {dir_current}")
    if not len(exts):
        print(f"*** NO FILES TO BE DELETED! ****")
        return False

    if echo:
        print("*** PLZ.CONFIRM THE FILES TO BE DELETED! ***")
        for i, item in enumerate(exts,1):
            print(f"{i:02}.{item}")

    if input('*** DELETE OK? [OK=1/NO=ENTER]'):
        for i, ext in enumerate(exts,1):
            os.remove(dir_target + ext)
            if echo:
                print(f"----> {i:02}.{ext} ... IS DELETED!")
        print()
    else:
        print(f"----> TERMINATED W/O DELETE.! \n")
        return False
    return True



# TODO 1: refactor variables, more effective
if __name__ == '__main__':
    main()
    pass
