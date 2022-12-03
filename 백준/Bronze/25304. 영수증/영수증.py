X = int(input())
N = int(input())
result = 0
for i in range(1, N + 1):
    a, b = map(int, input().split())
    price = a * b
    result += price

if result == X:
    print('Yes')
else:
    print('No')