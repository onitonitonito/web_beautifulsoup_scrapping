"""
#
#
#
"""
print(__doc__)


import os

F_NAME = '_1_thadd_article.pdb'
dir_work = os.path.dirname(__file__)
DESTIN_DIR = os.path.join(
    dir_work,
    *['_statics', '_temp', ''],)

# print(DESTIN_DIR)
# quit()



f = open(DESTIN_DIR + F_NAME, 'r', encoding='UTF-8')
a = f.read()        # 'str'
f.close()

b = a.split('\n^+^+^\n')        # list
c = b[1].split("'\\n")

print(a)

for n in range(1, len(c)):
    if '@donga.com' in c[n]:
        print('%s = %s ' % (n, c[n]))
        break

    else:
        print('%s = %s ' % (n, c[n]))
