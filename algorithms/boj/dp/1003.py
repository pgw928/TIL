import sys

input = sys.stdin.readline

t = int(input())

def sol(n):
    while True:
        if n in dp:
            print(dp[n][0], dp[n][1])
            break
        for k in range(max(dp),n+1):
            dp[k] = (dp[k-2][0]+dp[k-1][0], dp[k-2][1]+dp[k-1][1])

dp = {0:(1, 0), 1:(0, 1), 2:(1, 1), 3:(1, 2)}
for _ in range(t):
    n = int(input())
    sol(n)