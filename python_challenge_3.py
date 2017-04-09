guts = open("data3.txt").read()
c = []
guts = guts.replace('\n', '')
for i in range(1, len(guts)-7):
    if guts[i+3].islower() and guts[i-1].islower() and guts[i:i+3].isupper() and guts[i+4:i+7].isupper() and guts[i+7].islower():
        c.append(guts[i+3])
print("".join(c))
