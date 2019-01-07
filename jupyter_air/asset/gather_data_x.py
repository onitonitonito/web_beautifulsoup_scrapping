"""-------------------------
#
#
#
#"""
print(__doc__)


import os
import glob


PATH_HOME = os.getcwd()
PATHS_HERE = ['jupyter_air','asset']
PATHS_DATA = ['static', 'data']

path_data = os.path.join(PATH_HOME, *PATHS_DATA)
all_files = glob.glob(os.path.join(path_data, '*.csv'))

print(all_files)    # []
print(path_data.split('\\'))    # C:\\ ... \jupyter_air\\static\\data'


if __name__ == '__main__':

    for file_ in all_files:
        file_name = file_
        print(file_name)
