"""
# due to the differences results on Terminal & script_run
# for inserting root_dir, need 4 lines minimum
"""
import os, sys                                          # 1
root_name = "web_beautifulsoup_scrapping"               # 2
root = "".join(os.getcwd().partition(root_name)[:2])    # 3
sys.path.insert(0, root)                                # 4
import _assets.script_run
print(__doc__)


import _assets.configs as conf

# [print(func) for func in sd.__dir__() if not func.startswith("_")]
print(conf.dict_dirs.keys())

print()
[print(dir) for dir in sys.path]
