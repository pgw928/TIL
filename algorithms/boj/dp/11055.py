import sys

input = sys.stdin.readline
n = int(input())

A = list(map(int, input().split()))
dp = [[0,0] for _ in range(n)]
dp[0][0] = dp[0][1] = A[0]
k = 0
for i in range(1,n):
    dp[i][0], dp[i][1] = A[i], A[i]
    for j in range(i-1,-1,-1):
        if A[i]>dp[j][1] and dp[i][0]<A[i]+dp[j][0]:
            dp[i][0], dp[i][1] = A[i]+dp[j][0], A[i]

print(dp)
print(max([a for a, b in dp]))



