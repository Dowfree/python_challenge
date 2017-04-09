# -*- coding: utf-8 -*-
f1 = open("mean reversion.txt", 'r', encoding='utf-8')
f2 = open("mean reversion_1.txt", 'w',  encoding='utf-8')
guts = f1.read()
guts_1 = guts.replace('', 'fi')
guts_2 = guts_1.replace('/', 'ff')
guts_3 = guts_2.replace('¯ ', 'fl')
guts_4 = guts_3.replace('\n', ' ')
f2.write(guts_4)
f1.close()
f2.close()
