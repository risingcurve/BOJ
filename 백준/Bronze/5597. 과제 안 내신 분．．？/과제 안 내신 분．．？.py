ans = []

for i in range(28):
    ans.append(int(input()))

standard = []

for i in range(1, 31):
    standard.append(i)

for i in ans:
    if i in standard:
        standard.remove(i)

for i in standard:
    print(i)