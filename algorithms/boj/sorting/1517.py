import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(n-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]
            count += 1
print(A,count)


