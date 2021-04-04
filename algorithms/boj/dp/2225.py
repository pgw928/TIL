import sys; input = sys.stdin.readline
n, k = map(int, input().split())

dp = [[0]*(n+1)  for _ in range(k)]
for j in range(n+1):
    dp[0][j] = 1
for i in range(1,k):
    dp[i][0] = 1

for i in range(1, k):
    for j in range(1, n+1):
        dp[i][j] = sum(dp[i-1][:j+1])
for d in dp:
    print(d)

print(dp[-1][-1]%1_000_000_000)