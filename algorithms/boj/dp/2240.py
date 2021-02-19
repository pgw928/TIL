import sys
input = sys.stdin.readline

t, w = map(int, input().split())
A = [int(input()) for _ in range(t)]

dp = [[0]*(t+1) for _ in range(w+1)]

for row in range(w+1):
    for col in range(1, t+1):
        c = 1 if A[col - 1] == row % 2 + 1 else 0
        if row ==0:
            dp[row][col] = dp[row][col-1]+ c
            continue
        dp[row][col] = max(dp[row-1][col-1], dp[row][col-1]) + c

print(max([row[-1] for row in dp]))