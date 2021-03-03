import sys
input = sys.stdin.readline

n = int(input())
h_w = [list(map(int, input().split())) for _ in range(n)]

pts, rank = {i:1 for i in range(n)}, [0]*n

for i in range(n-1):
    h_i, w_i = h_w[i]
    for j in range(i+1, n):
        h_j, w_j = h_w[j]
        if h_i > h_j and w_i > w_j:
            pts[j] += 1
        elif h_i < h_j and w_i < w_j:
            pts[i] += 1
print(' '.join(tuple(map(str, pts.values()))))




