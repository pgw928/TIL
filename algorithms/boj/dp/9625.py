import sys
n = int(sys.stdin.readline())

dp = {0:(1,0), 1:(0,1), 2:(1,1)}


if n<=2:
    a, b = dp[n]
    print(a, b)
else:
    for i in range(3, n+1):
        a, b = dp[i-1]
        dp[i] = (b ,a+b)
    a, b = dp[n]
    print(a, b)

