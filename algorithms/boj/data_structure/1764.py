import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A = set()
for _ in range(n):
    A.add(input().strip())

B = set()
for _ in range(m):
    B.add(input().strip())

C = sorted(list(A & B))
print(len(C))
for c in C:
    print(c)
