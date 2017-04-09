result = [1]

for i in range(30):
    count = 1          # 初始和重置字符计数器
    key = result       # 重置数字为上个循环结果
    result = []        # 重置储存数组
    letter = key[0]    # 初始字符
    for index in range(len(key)):
        if index == len(key)-1:
            result.append(count)
            result.append(letter)
        elif key[index] == key[index+1]:
            count += 1
        elif key[index] != key[index+1]:
            result.append(count)
            result.append(letter)
            count = 1
            letter = key[index+1]

print(len(result))
print('http://www.pythonchallenge.com/pc/return/5808.html')
