# -*- coding: utf-8 -*-
line = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
line = 'map'
a = []
newline = []
for i in range(0, len(line)):
    a.append(ord(line[i]))
    if 97 <= a[i] <= 120:
        a[i] += 2
    elif a[i] == 121 or a[i] == 122:
        a[i] -= 24
    newline.append(chr(a[i]))
print("".join(newline))
