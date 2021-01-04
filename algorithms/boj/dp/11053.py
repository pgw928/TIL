import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

dp= [1 for _ in range(len(A))]

for i in range(1, N):
    for j in range(i):
        if (A[i] > A[j]) and (dp[i]<= dp[j]):
            dp[i] = dp[j] + 1
print(A, dp)
print(max(dp))
