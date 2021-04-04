import sys; input = sys.stdin.readline
n = int(input())
dp2m = [[0]*3 for _ in range(n+1)]
dp2M = [[0]*3 for _ in range(n+1)]
a1, b1, c1 = 0, 0, 0
a2, b2, c2 = 0, 0, 0
for i in range(1,n+1):
    tmp = list(map(int, input().split()))
    aa1 = tmp[0] + max(a1, b1)
    bb1 = tmp[1] + max(a1, b1, c1)
    cc1 = tmp[2] + max(b1, c1)

    aa2 = tmp[0] + min(a2, b2)
    bb2 = tmp[1] + min(a2, b2, c2)
    cc2 = tmp[2] + min(b2, c2)

    a1, b1, c1 = aa1, bb1, cc1
    a2, b2, c2 = aa2, bb2, cc2

print(max(a1, b1, c1), min(a2, b2, c2))
