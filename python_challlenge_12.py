
fp = open('evil2.gfx', 'rb')
content = fp.read()
fp.close()

for i in range(5):
    f = open('chanllenge12_%d' % i, 'wb')
    f.write(content[i::5])
    f.close()

print('http://www.pythonchallenge.com/pc/return/disproportional.html')
