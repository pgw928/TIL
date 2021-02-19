import sys

input = sys.stdin.readline
n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]

result = [0]*(n+1)

for i in range(n-1,-1 ,-1):
    a, b = A[i]
    if a+i<=n:
        result[i] = b + max(result[i+a:])

print(max(result))
