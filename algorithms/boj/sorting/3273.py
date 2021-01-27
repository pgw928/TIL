import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
A.sort()
x = int(input())

score = 0
l = len(A)
i = l - 1
j = 0
while i > j:

    s = A[i] + A[j]
    if s > x:
        i-= 1
    elif s == x:
        score += 1
        i -= 1
        j += 1
    elif s < x:
        j += 1
print(score)

