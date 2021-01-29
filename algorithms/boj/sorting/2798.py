import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = tuple(map(int, input().split()))
print(max([A[i]+A[j]+A[k] for i in range(1,n-2) for j in range(i+1, n-1) for k in range(j+1, n) if A[i]+A[j]+A[k]<=m]))
