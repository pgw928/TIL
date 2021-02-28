import sys

n, m = map(int, sys.stdin.readline().split())

dp = []
dp.append([0] * (m + 1))
dp.append([0] + [1] * m)
for _ in range(n - 1):
    dp.append([0, 1] + [0] * (m - 1))

for i in range(2, n + 1):
    for j in range(2, m + 1):
        dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j]

print(dp[n][m] % 1000000007)