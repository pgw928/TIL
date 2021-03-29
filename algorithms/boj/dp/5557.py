import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
arr = list(map(int, input().split()))

dp = [[0]*21 for _ in range(len(arr)-1)]
print(dp)
dp[0][arr[0]] = 1
for i in range(1, len(arr)-1):
    for j in range(21):
        if 0 <= j+arr[i] <= 20:
            dp[i][j] += dp[i-1][j+arr[i]]
        if 0<=j-arr[i] <= 20:
            dp[i][j] += dp[i-1][j-arr[i]]

for d in dp:
    print(d)
print(dp[-1][arr[-1]])
