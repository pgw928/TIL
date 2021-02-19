import sys

input = sys.stdin.readline
check = [[0]*101 for _ in range(101)]

for _ in range(4):
    x, y, xx, yy = tuple(map(int, input().split()))
    for i in range(x, xx):
        for j in range(y, yy):
            check[i][j] = 1

s = 0
for r in check:
    s += sum(r)
print(s)

