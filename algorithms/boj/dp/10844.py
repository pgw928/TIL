import sys

n = int(sys.stdin.readline())

dp = {1:[0, 1, 1, 1, 1, 1,1,1,1,1]}

def sol(n):
    while True:
        if n in dp:
           return sum(dp[n])%(10**9)
        for i in range(max(dp)+1, n+1):
            tmp = [0]*10
            tmp[0], tmp[-1] = dp[i-1][1], dp[i-1][-2]
            for j in range(1,9):
                tmp[j] = dp[i-1][j-1] + dp[i-1][j+1]
            dp[i] = tmp

print(sol(n))