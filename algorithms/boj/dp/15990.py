import sys; input = sys.stdin.readline
nn = []
for _ in range(int(input())):
    nn.append(int(input()))

n = max(3, max(nn))
dp = [[0] * (n + 1) for _ in range(3)]
dp[0][1], dp[1][2] = 1, 1
dp[0][3], dp[1][3], dp[2][3] = 1, 1, 1

for j in range(4, n+1):
    dp[0][j] = (dp[1][j-1] + dp[2][j-1])
    dp[1][j] = (dp[0][j-2] + dp[2][j-2])
    dp[2][j] = (dp[0][j-3] + dp[1][j-3])

for k in nn:
    print((dp[0][k]+dp[1][k]+dp[2][k])%1_000_000_009)