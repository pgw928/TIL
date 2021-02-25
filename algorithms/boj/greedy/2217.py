import sys
input = sys.stdin.readline
n = int(input())
rope = sorted([int(input()) for _ in range(n)], reverse=True)

M = []
for i in range(1,n+1):
    M.append(i*rope[i-1])

print(max(M))
