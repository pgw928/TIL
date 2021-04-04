import sys; input = sys.stdin.readline
n = int(input())
dp = [[0]*3 for _ in range(n+1)]

rgb = [tuple(map(int, input().split())) for _ in range(n)]
# dp[0][0] = rgb[0][1]
# dp[0][1] = rgb[0][2]
# dp[0][2] = rgb[0][3]
for d in rgb:
    print(d)
for i in range(1, n):
    dp[i][0] = rgb[i-1][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = rgb[i-1][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = rgb[i-1][2] + min(dp[i-1][1], dp[i-1][0])


dp[-1][0] = rgb[][] + min(dp[i-1][1], dp[i-1][2])

dp[-1][1] = rgb[][] + min(dp[i-1][0], dp[i-1][2])
dp[-1][2] = rgb[][] + min(dp[i-1][1], dp[i-1][0])


for d in dp:
    print(d)