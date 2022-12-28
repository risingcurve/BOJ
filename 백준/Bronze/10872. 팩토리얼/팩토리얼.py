def recur(n):
    if n >= 2:
        return n * recur(n-1)
    else:
        return 1

N = int(input())
print(recur(N))