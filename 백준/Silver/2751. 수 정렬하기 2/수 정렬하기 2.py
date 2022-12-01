import sys

input = sys.stdin.readline
N = int(input())

basket = []
for n in range(N):
    basket.append(int(input()))

new_basket = sorted(basket)

for i in new_basket:
    print(i)