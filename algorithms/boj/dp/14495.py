n = int(input())

dp = {1:1, 2:1, 3:1}

for i in range(4,n+1):
    dp[i] = dp[i-1] + dp[i-3]

print(dp[n])
