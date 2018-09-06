import os

F_NAME = '_1_thadd_article.pdb'
DESTIN_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    '_static', '_temp', '')

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
