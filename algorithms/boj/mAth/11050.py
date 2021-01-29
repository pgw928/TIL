import sys

n, r = map(int, sys.stdin.readline().split())
r = min(n-r, r)
res = 1
for i in range(1, r + 1):
    res *= ((n - i + 1) / (r - i + 1))

print(int(res))
