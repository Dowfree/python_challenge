import zipfile

file = zipfile.ZipFile('channel.zip', 'r')
num = '90052'
comment = []
while True:
    fp = open(r'C:\Users\free\PycharmProjects\python_challenge\channel\%s.txt' % num)
    data = fp.read()
    num = "".join([i for i in data if i.isdigit()])
    fp.close()
    if not num:
        break
    comment.append(bytes.decode(file.getinfo(num+".txt").comment))
    print(data, num)
print("".join(comment))
