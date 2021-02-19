import sys

input = sys.stdin.readline
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1,-1 ,-1):
    a, b = A[i]
    if a+i>=n+1:
        A[i][1] = 0
    elif a+i<n+1:
        # A[i][1] += max([A[j][1] for j in range(a+i,n)], default=0)
        A[i][1] += A[i+a-1][1]
    print(A)
print(max([A[j][1] for j in range(n)]))