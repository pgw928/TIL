import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

sum = 0
for a, b in zip(A,B):
    sum += (a*b)
