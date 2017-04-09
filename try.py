n, a = 1, [1]
while n < 10:
    b = a
    a = []
    for i in range(1, len(b)):
        a.append(b[i] + b[i - 1])
    a = [1] + a + [1]
    print(a)
    n += 1




