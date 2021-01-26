import sys

input = sys.stdin.readline

n = int(input())

A = [ int(input()) for _ in range(n)]

memo = {0:[0, 0],1:[A[0], 0]}

for i in range(2, len(A)+1):
    memo[i] = [A[i-1] + max(memo[i-2]) , A[i-1] + memo[i-1][0]]


print(max(memo[n]))
