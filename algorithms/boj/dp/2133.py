import sys
n = int(sys.stdin.readline())
if n%2==1:
    print(0)
else:
    dp = [0] * (n // 2 + 1)
    a, b = 3, 2
    dp[1] = 3
    for i in range(2, n//2+1):
        dp[i] = dp[i-1]*3 + sum(dp[1:i-1]*2) +2
    print(dp[n//2])
