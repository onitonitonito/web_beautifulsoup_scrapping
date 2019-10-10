"""
# 마크다운이 포함 된, Python 스크립트를 HTML 형태의 핸드아웃 페이지로 변환해 주는
# 패키지를 소개해 드립니다.
# https://github.com/danijar/handout
"""
print(__doc__)

import handout
import matplotlib.pyplot as plt
import numpy as np

# DESTIN_DIR = './handout_doc/'     # Root Sub_folder
DESTIN_DIR = 'handout_doc'          # Sub_folder

""" Start your handout with an output directory """
# doc = handout.Handout('/tmp/handout')
doc = handout.Handout(DESTIN_DIR)

""" Print text and Variables. """
for index in range(3):
    doc.add_text(f'Interation ... {index}')

doc.show()

""" Insert matplotlib figure """
fig, ax = plt.subplots(1,1, figsize=(4,3))
fig.tight_layout()

doc.add_figure(fig)
doc.show()
