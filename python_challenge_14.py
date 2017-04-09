from functools import reduce
from PIL import Image

l = [[i, i-1, i-1, i-2] for i in range(100, 1, -2)]
l = reduce(lambda x, y: x+y, l)     # 此处的+为列表扩展，将为l转化为一个列表
num = reduce(lambda x, y: x+y, l)   # 此处的+为数字相加，证明此列表之和为10000
# print(num)

im = Image.open('wire.png')
im_new = Image.new(im.mode, (100, 100))


dire = [(1, 0),  # > (x+1, y) right
        (0, 1),  # v (x, y+1) down
        (-1, 0),  # < (x-1, y) left
        (0, -1),  # ^ (x, y-1) up
        ]

# init
v = 0
im_index = 0
im_new_pos = (-1, 0)
for times in l:
    for i in range(times):
        # pos will out of index if reset position after setting color
        im_new_pos = tuple(
            map(lambda x, y: x + y, im_new_pos, dire[v]))  # (res_pos[0] + dire[v][0], res_pos[1] + dire[v][1])
        im_new.putpixel(im_new_pos, im.getpixel((im_index, 0)))
        im_index += 1

    v = (v + 1) % 4  # j + 1 if j != 4 else 0

im_new.show()
# im_new.save('challenge14_result.png')
print('http://www.pythonchallenge.com/pc/return/cat.html')
