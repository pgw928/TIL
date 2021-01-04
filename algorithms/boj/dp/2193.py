import sys

N = int(sys.stdin.readline())

dp = [1, 1, 2]

for i in range(3, N+1):
    dp.append(dp[i-2]+dp[i-1])

print(dp[N-1])