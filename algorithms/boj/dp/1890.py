import sys; input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

count = 0
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i < graph[i][j] + i < n :
            dp[graph[i][j] + i][j] += dp[i][j]
        if j < graph[i][j] + j < n:
            dp[i][graph[i][j] + j] += dp[i][j]
print(dp[n-1][n-1])