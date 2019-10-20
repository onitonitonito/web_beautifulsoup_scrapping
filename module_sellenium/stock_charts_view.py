"""
# stock_charts_view /pstaticNet - jupyter notebook conversion
# config_stocks.py 에서 변수를 가져옴 (종목명/코드)
"""

import skimage
import numpy as np
import matplotlib.pyplot as plt

import assets.script_run
from assets.config_stocks import code_stock, URL, sidecode
from assets.functions_class import set_font_hanguel_graph

print(__doc__)

# pyplot 그래프 상, 한글폰트 깨짐 방지
set_font_hanguel_graph()

# 글로벌 변수 = names, codes 정의.
(names, codes) = list(code_stock.keys()), list(code_stock.values())
targets = ['day','week','month3','year','year3','year5','year10']
start, end = (0, 6)

def main():
    """ 6개 ~ 최대12개 챠트만 나열해서 봅니다. 그게 제일, 보기 적당해"""
    global start, end
    save_chart_only = False

    # 확인할 종목명, 코드를 보여준다.
    show_names_codes(start, end)

    # only save all = True / just watch = Flase
    save_or_show(save_chart_only)

def show_names_codes(start, end):
    """ HELPER() for main() : 관심종목명(코드)를 보여줌 """
    global names, codes
    names_partial = names[start:end]
    codes_partial = codes[start:end]

    print(f"\nTargets = {targets}", flush=True)
    print("========"*5, flush=True)
    for i, name in enumerate(names_partial):
        print(f" {i+1:02}. {name} ({codes_partial[i]})", flush=True)
    print("========"*5, flush=True)
    print("* 변경:'config_stocks.py' 의 변수를 수정.\n\n", flush=True)

def save_or_show(save_chart_only):
    """ HELPER() for main() : 저장만 하든지, 보기만 하든지 """
    global targets, start, end

    for i, target in enumerate(targets):
        proceed = f"{i+1}/{len(targets)}"  # 진행정도
        question = f"\n\nDraw '{target}'graph({proceed})? ... [OK=Ent./NO=1]"

        if save_chart_only:
            show_charts_axes(target, start, end)
            plt.savefig(fname=f"./statics/{i:02}_{target}.png")
        else:
            if not input(question).startswith("1"):
                show_charts_axes(target, start, end)
                plt.show()
            else:
                print(f" ***** '{target}' charts are skipped! *****")

def get_images_nparray(target, start, end):
    """
    HELPER() for show_charts_axes() :목적챠트(target)에 대해 start~end 범위
    skimage obj. array 반납
    """
    global names, codes
    images_nparray = []
    for i, name in enumerate(names[start:end]):
        img_url = f"{URL}/{target}/{codes[i]}.png?sidcode={sidecode}"
        im_array = skimage.io.imread(img_url)
        images_nparray.append(im_array)
    return images_nparray

def show_charts_axes(target, start, end):
    """ 헬퍼함수를 사용해서 targer 과 start_end를 받아서 챠트를 출력한다. """
    global names, codes
    images = get_images_nparray(target, start, end)
    names = names[start:end]
    codes = codes[start:end]

    (cols, rows) = (2, int(len(names)/2))     # (2 , 6)
    fig, ax = plt.subplots(ncols=cols, nrows=rows, figsize=(18,rows*6))

    count = 0
    for row in range(rows):
        for col in range(cols):
            # print(row,col)   # ... for test
            ax[row,col].imshow(images[count])
            ax[row,col].set_title(f"{names[count]} ({codes[count]}) by {target}")
            count += 1
    plt.tight_layout(pad=0.1)

# TODO 1: names and charts are not matched -- should be corrected!
# TODO 2: refactor variables, more effective

if __name__ == '__main__':
    main()
