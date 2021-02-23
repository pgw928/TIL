import sys

input = sys.stdin.readline
n, k = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]

for row in range(1, n+1):
    wi, vi = A[row - 1]
    for col in range(1, k+1):
        if wi <= col:
            dp[row][col] = max(vi+dp[row-1][col-wi], dp[row-1][col])
        else:
            dp[row][col] = dp[row-1][col]

for d in dp:
    print(d)
print((dp[-1][-1]))