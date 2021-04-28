import sys; input = sys.stdin.readline
from collections import deque
from heapq import heappush, heappop
n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tree = []
for _ in range(m):
    x, y, z = map(int, input().split())
    heappush(tree,(z, x-1, y-1))

energy = [[5]*n for _ in range(n)]
dy = [-1, 1, 0, 0, 1, -1, 1, -1] 
dx = [0, 0, -1, 1, 1, 1, -1, -1]
while k:
    # 봄, 여름
    l = len(tree)
    tmp = []
    for _ in range(l):
        z, x, y = heappop(tree)
        if z <= energy[x][y]:
            energy[x][y] -= z
            tmp.append((z+1, x, y))
        else:
            energy[x][y] += z//2
            l -= 1
    # 가을
    for i in range(l):
        z, x, y = tmp[i]
        if z%5==0:
            for s in range(8):
                a, b = x+dx[s], y+dy[s]
                if 0<=a<n and 0<=b<n:
                    heappush(tree, (1, a, b))
        heappush(tree, (z, x, y))       
    # 겨울
    for i in range(n):
        for j in range(n):
            energy[i][j] += graph[i][j]
    k -= 1
    print(tree)
    for e in energy:
        print(e)
print(len(tree))