import sys
input = sys.stdin.readline
n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])

M = max([a[1] for a in arr])
A = [0]*(M+1)
dp = [0]*(M+1)
for a,b in arr:
    if A[a]==0:
        if a==b:
            dp[a] += 1
        else:
            A[a] = b

print(A, dp)

for i in range(M, -1 ,-1):
    if A[i]!=0:
        if A[i]!=i:
            dp[i] += 1 + max(dp[A[i]:])
        elif i==M:
            dp[i] += 1
        else:
            dp[i] += max(dp[i+1:])+1
    if A[i]==0 and i<M:
        dp[i]+=dp[i+1]
    print(dp)
print(dp)
print(max(dp))
