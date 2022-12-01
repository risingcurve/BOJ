arr = list(map(int, input().split()))

standard = [1, 1, 2, 2, 2, 8]

ans = []

for i in range(6):
    if arr[i] == standard[i]:
        ans.append(0)
    else:
        a = standard[i] - arr[i]
        ans.append(a)


print(*ans)