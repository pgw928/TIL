import sys

input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))

dp = [0]*(N+1)


dp[1] = p[0]
dp[2] = min(2*p[0], p[1])

for i in range(3,N+1):
    dp[i] = p[i-1]
    for j in range(i//2+1):
        dp[i] = min(dp[i], dp[j]+dp[i-j] )

print(dp[N])