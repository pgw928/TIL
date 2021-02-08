import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [[0, 0] for _ in range(n+1)]
dp[1][0], dp[1][1] = wine[0], wine[0]

for i in range(2,n+1):
    dp[i][0] = max(max(dp[i-2]) + wine[i-1], dp[i-1][1])
    dp[i][1] = dp[i-1][0] + wine[i-1]

print(max(dp[-2][0] ,max(dp[-1])))