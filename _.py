"""
# due to the differences results on Terminal & script_run
# for inserting root_dir, need 4 lines minimum
"""
# root path 를 sys.path.insert 시키기 위한 코드 ... 최소 4줄 필요------------
import os, sys                                                          # 1
root_name = "web_beautifulsoup_scrapping"                               # 2
root = "".join(os.path.dirname(__file__).partition(root_name)[:2])+"\\" # 3
sys.path.insert(0, root)                                                # 4
# -------------------------------------------------------------------------

import _assets.script_run
import _assets.configs as conf

print(__doc__)


# [print(func) for func in sd.__dir__() if not func.startswith("_")]
print(conf.dirs_dict.keys())

print()
[print(dir) for dir in sys.path]
