from urllib import request
num = '27709'
i = 0
while True:
    f = request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % num, timeout=100)
    data = f.read().decode('utf-8')
    num = "".join([i for i in data if i.isdigit()])
    i += 1
    print(data, num, i)
