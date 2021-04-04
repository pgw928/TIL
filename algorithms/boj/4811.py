import sys; input = sys.stdin.readline

dp = [0]*(31)
dp[1], dp[2] = 1, 2
for i in range(3, 31):
    dp[i] = 2*dp[i-1] + 2*dp[i-2] + 2*dp[i-3]
while True:
    n = int(input())
    if n==0:
        break
    print(dp[n])


