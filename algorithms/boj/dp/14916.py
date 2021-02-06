import sys

n= int(sys.stdin.readline())

dp = {1:-1, 2: 1, 3:-1, 4:2, 5:1, 6:3}

def sol(k):
    if k in dp:
        return dp[k]
    for i in range(7,n+1):
        if dp[i-5]==-1:
            dp[i] = dp[i-2]+1
        elif dp[i-2]==-1:
            dp[i] = dp[i-5]+1
        else:
            dp[i] = min(dp[i-2]+1, dp[i-5]+1)
    return dp[k]

print(sol(n))