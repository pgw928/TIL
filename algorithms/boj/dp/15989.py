import sys
input = sys.stdin.readline
t = int(input())


def sol(n):
    dp = [1] + [0]*n
    for i in range(1,4):
        for j in range(i,n+1):
            dp[j] += dp[j-i]
    return dp[-1]

for _ in range(t):
    n = int(input())
    print(sol(n))