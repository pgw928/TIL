n, k = map(int, input().split())
dp = [0 for i in range(k + 1)]
dp[0] = 1

coins = [int(input()) for _ in range(n)]

for coin in coins:
    for j in range(1, k + 1):
        if j - coin >= 0:
            dp[j] += dp[j - coin]
print(dp[k])