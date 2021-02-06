import sys

n = int(sys.stdin.readline())

dp = {0:0, 1:1}


def sol(k):
    if k in dp:
        return dp[k]
    else:
        dp[k] = sol(k-1) + sol(k-2)

    return dp[k]
print(sol(n))