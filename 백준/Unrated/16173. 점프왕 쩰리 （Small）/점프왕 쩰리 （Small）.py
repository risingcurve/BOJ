n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dp = [[False] * n for _ in range(n)]
dp[0][0] = True

for i in range(n):
    for j in range(n):
        if dp[i][j] and board[i][j] > 0:
            if i + board[i][j] < n:
                dp[i + board[i][j]][j] = True
            if j + board[i][j] < n:
                dp[i][j + board[i][j]] = True

if dp[n - 1][n - 1]:
    print("HaruHaru")
else:
    print("Hing")
