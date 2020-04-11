"""
# stock_charts_view /pstaticNet - jupyter notebook conversion
# config_stocks.py 에서 변수를 가져옴 (종목명/코드)
"""
import random
import skimage.io
import matplotlib.pyplot as plt

import assets.script_run
from assets.config_stocks import *
from assets.functions_class import get_today_header
from assets.functions_class import set_font_hanguel_graph

print(__doc__)

# pyplot 그래프 상, 한글폰트 깨짐 방지
set_font_hanguel_graph()

# 글로벌 변수 = names, codes 정의.
header = get_today_header()             # 05Dec(Thu)AM0803_2017

def main():
    """ 6개 ~ 최대12개 챠트만 나열해서 봅니다. 그게 제일, 보기 적당해"""
    global index_partial
    # 확인할 종목명, 코드를 보여준다.
    show_dict()
    # only save all = True / just watch = Flase
    save_chart_only = is_save_only()

    # show_names_codes(index_partial) --> global
    index_partial = get_index_partial()

    save_or_show(save_chart_only)


def get_index_partial():
    """ index_partial 을 input 입력 받는다. """
    print()
    answer = input(
                "idx_array를 ','구분 4개 이상 입력 짝수로 입력 (예) 4,3,1,2\n" +
                "or [ENTER]=기본 처음 4개 출력 [1,2,3,4]와 동일\n :    "
                ).strip()
    if answer[0:1].isnumeric():
        print([int(idx)-1 for idx in answer.split(",")])
        return [int(idx)-1 for idx in answer.split(",")]
    else:
        print([idx for idx in range(4)])
        return [idx for idx in range(4)]

def is_save_only():
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

def save_or_show(save_chart_only=False):
    """ HELPER() for main() : 저장만 하든지, 보기만 하든지 """
    global targets, header

    for i, target in enumerate(targets):
        proceed = f"{i+1}/{len(targets)}"  # 진행정도 표시
        question = f"\n\nDraw '{target}'graph({proceed})? ... [OK=Ent./NO=1]"

        if save_chart_only:
            # save all charts designated, properly 4 charts
            print(f"\n... '{i:02}.{target}' chart is saved", flush=True)
            show_charts_axes(target, index_partial)
            plt.savefig(fname=home_works + f"{header}_{i:02}_{target}.png")
        else:
            if not input(question).startswith("1"):
                show_charts_axes(target, index_partial)
                plt.show()
            else:
                print(f" ***** '{target}' charts are skipped! *****")




# TODO 1: refactor variables, more effective
if __name__ == '__main__':
    main()
