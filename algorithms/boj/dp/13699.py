import sys

n= int(sys.stdin.readline())

dp = {0:1, 1:1, 2:2, 3:5}

if n in dp:
    print(dp[n])
else:
    s = 0
    for i in range(4,n+1):
        dp[i] = sum([dp[j]*dp[i-1-j] for j in range(i)])
    print(dp[n])

