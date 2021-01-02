import sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
def solution(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n==3:
        return 1
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        if i%6 == 0:
            dp[i] = min(1 + dp[i//3], 1 + dp[i//2], 1 + dp[i-1])
        elif i%3 == 0:
            dp[i] = min(1 + dp[i//3], 1 + dp[i-1])
        elif i%2 == 0:
            dp[i] = min(1 + dp[i//2], 1 + dp[i-1])
        else:
            dp[i] = dp[i-1] + 1
    return dp[n]

print(solution(n))