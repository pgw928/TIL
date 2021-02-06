import sys

n = int(sys.stdin.readline())

dp = {1:4, 2:6, 3:10}


def sol(k):
    if k in dp:
        return dp[k]
    else:
        dp[k] = sol(k-1) + sol(k-2)

    return dp[k]
print(sol(n))