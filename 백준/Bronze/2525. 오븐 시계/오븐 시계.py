A, B = map(int, input().split())
C = int(input())

if B + C >= 60:
  A = A + ((B + C) // 60)
  B = (B + C) % 60
  if A >= 24:
    A = A - 24

else:
  B = B + C
  if A >= 24:
    A = A - 24

ans = f'{A} {B}'
print(ans)