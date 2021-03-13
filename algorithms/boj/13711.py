import sys; input = sys.stdin.readline
n = int(input())
A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])