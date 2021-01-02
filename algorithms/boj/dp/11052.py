import sys

input = sys.stdin.readline

N = int(input())

P = list(map(int, input().split()))

dp = [0]* (N+1)
dp[0] = 0
dp[1] = P[0]                # 1
dp[2] = max(P[1], 2*P[0])   # 2


for i in range(3, N+1):
    dp[i] = P[i-1]
    for j in range(i):
        dp[i] = max(dp[i], dp[j]+dp[i-j] )

print(dp[N])
