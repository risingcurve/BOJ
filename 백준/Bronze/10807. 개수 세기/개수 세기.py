N = int(input())

arr = list(map(int, input().split()))

v = int(input())

a = 0
for i in arr:
    if i == v:
        a += 1

print(a)