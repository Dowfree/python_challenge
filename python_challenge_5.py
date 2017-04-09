# -*- coding: utf-8 -*-
# using pickle module

import pickle

fp = open('data5.txt', 'rb')
data = pickle.load(fp)
for i in data:
    for j in i:
        if j[0] == ' ':
            print(' '*j[1], end='')
        else:
            print('#'*j[1], end='')
    print()
fp.close()
