import sys

input = sys.stdin.readline
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
M = [0]*(n+1)
for i in range(n-1,-1 ,-1):
    a, b = A[i]

    if i + a> n:
        A[i][1] = 0
        M[i] = M[i+1]

    elif i + a <= n:
        A[i][1] += M[i+a]
        M[i] = max(A[i][1], M[i+1])

print(M[0])