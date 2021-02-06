import sys
input= sys.stdin.readline

t = int(input())

dp = {1:1, 2:1, 3:1}


def sol(k):
    if k in dp:
        return dp[k]
    else:
        for i in range(4,k+1):
            dp[i] = dp[i-2] + dp[i-3]
    return dp[k]

for _ in range(t):
    n = int(input())
    print(sol(n))