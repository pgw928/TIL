import sys; input = sys.stdin.readline
from collections import deque

dz, dy, dx = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
def bfs(start):
    dq = deque()
    dq.append(start)
    z, y, x = start
    visited[z][y][x] = 0
    while dq:
        z, y, x = dq.popleft()
        for k in range(6):
            zz, yy, xx = z+dz[k], y+dy[k], x+dx[k]
            if 0<=zz<l and 0<=yy<r and 0<=xx<c:
                if graph[zz][yy][xx]=='.' and visited[zz][yy][xx]==-1:
                    dq.append((zz, yy, xx))
                    visited[zz][yy][xx] = visited[z][y][x] + 1
                elif graph[zz][yy][xx]=='E' and visited[zz][yy][xx]==-1:
                    return f'Escaped in {visited[z][y][x]+1} minute(s).'
    return 'Trapped!'



while True:
    l, r, c = map(int, input().split())
    if l==0:
        break
    graph = [[] for _ in range(l)]
    idx = 0
    for _ in range(l*r+l):
        tmp = input().strip()
        if tmp:
            graph[idx].append(tmp)
        else:
            idx += 1
    visited = [[[-1]*c for _ in range(r)] for _ in range(l)]
    bk_pt = False
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k]=='S':
                    start = (i, j, k)
                    bk_pt = True
                    break
            if bk_pt:
                break
        if bk_pt:
            break
    print(bfs(start))