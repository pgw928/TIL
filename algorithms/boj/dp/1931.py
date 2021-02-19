import sys

input = sys.stdin.readline
n = int(input())
A = []
for i in range(n):
    a, b = map(int, input().split())
    A.append([b-a, 1])


for i in range(n-1,-1 ,-1):
    a, b = A[i]
    if a+i>n:
        A[i][1] = 0
    elif a+i<=n:
        A[i][1] += max([A[j][1] for j in range(a+i,n)], default=0)

print(max([A[j][1] for j in range(n)]))