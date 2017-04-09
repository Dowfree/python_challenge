from PIL import Image

im = Image.open('cave.jpg')
w = im.size[0]
h = im.size[1]
odd = even = Image.new(im.mode, (int(w/2), int(h/2)))

for x in range(w):
    for y in range(h):
        if (x + y) % 2 == 0:
            even.putpixel((int(x/2), int(y/2)), im.getpixel((x, y)))
        else:
            odd.putpixel((int(x/2), int(y/2)), im.getpixel((x, y)))

even.show()
odd.show()
print('http://www.pythonchallenge.com/pc/return/evil.html')
