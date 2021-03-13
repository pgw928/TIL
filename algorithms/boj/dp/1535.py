import sys; input = sys.stdin.readline
n = int(input())
energy = tuple(map(int, input().split()))
joy = tuple(map(int, input().split()))
dp = [[0]*(100) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 100):
        if  j - energy[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j-energy[i-1]] + joy[i-1], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

for d in dp:
    print(d)
print(dp[-1][-1])