import sys; input = sys.stdin.readline
from collections import deque
r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
water = []
for i in range(r):
    for j in range(c):
        if graph[i][j]=='*':
            water.append((i,j))
        elif graph[i][j]=='D':
            beaver = i, j
        elif graph[i][j]=='S':
            hedgehog = i, j
graph[hedgehog[0]][hedgehog[1]] = '.'

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(start):
    global water
    dq= deque()
    dq.append((start[0], start[1], 0))
    visited = [start]
    flag = 0
    while dq:
        yy, xx, cu = dq.popleft()
        if (yy, xx) == beaver:
            return cu
        if water and flag==cu:
            tmp = []
            for i in range(len(water)):
                y, x = water[i]
                for k in range(4):
                    b, a = y+dy[k], x+dx[k]
                    if 0 <= b < r and 0 <= a < c and graph[b][a]=='.':
                        graph[b][a] = '*'
                        tmp.append((b, a))
            water = tmp
            flag += 1

        for k in range(4):
            b, a = yy+dy[k], xx+dx[k]
            if (0 <= b < r and 0 <= a < c) and (graph[b][a] == '.' or graph[b][a]=='D') and ((b,a) not in visited):
                dq.append((b, a, cu+1))
                visited.append((b, a))
    return 'KAKTUS'

print(bfs(hedgehog))