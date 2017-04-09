# -*- coding:utf-8 -*-
# 网页内容下载和图片处理

import urllib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

# urllib.request.urlretrieve("http://www.pythonchallenge.com/pc/def/oxygen.png", 'oxygen.png')
lena = mpimg.imread('oxygen.png')  # lena是float32型的数组，范围是0-1
# plt.imshow(lena)
# plt.show()

im = Image.open('oxygen.png')   # 此时读入的im是PngImageFile形式，需要用np转化为数组形式
im_array = np.array(im)   # im.array是uint8形式（无符号整数， 0-255）
# print(im_array.shape)
# print(im_array[:, 10, 1])
print("".join([chr(i) for i in im_array[43, 0:609, 1]]))  # 黑白条码部分纵坐标是43—51，横坐标是0-607
key =  [chr(im_array[43, i, 1]) for i in range(0, 608, 7)]
print("".join(key))
num = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join([chr(i) for i in num]))
