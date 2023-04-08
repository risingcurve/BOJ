n = int(input())

# 최소한의 봉지 개수를 저장하는 변수를 큰 값으로 초기화
min_count = float('inf')

# 5kg 봉지로 모두 담는 경우부터 시작해서
for i in range(n // 5, -1, -1):
    # 남은 무게가 3의 배수인 경우
    if (n - (5 * i)) % 3 == 0:
        # 5kg 봉지와 3kg 봉지의 개수를 합산
        count = i + ((n - (5 * i)) // 3)
        # 최소 개수를 구함
        min_count = min(min_count, count)

# 정확히 Nkg을 만들 수 없는 경우 -1 출력
if min_count == float('inf'):
    print(-1)
else:
    print(min_count)
