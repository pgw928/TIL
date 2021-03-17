import sys; input = sys.stdin.readline
from collections import deque
from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for i in range(n)]
virus_lst = []
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            graph[i][j] = 0
            virus_lst.append((i, j))

combs = combinations(virus_lst, m)
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(start_nodes, g):
    dq = deque()
    dq.extend(start_nodes)
    for i, j in start_nodes:
        g[i][j] = -1

    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<n and 0<=a<n and g[b][a]==0:
                g[b][a] = g[y][x] - 1
                dq.append((b,a))
    mm = 25000
    for i in range(n):
        for j in range(n):
            if g[i][j]==0:
                return -1
            mm = min(g[i][j], mm)

    return -mm-1


result = []
for comb in combs:
    result.append(bfs(comb, deepcopy(graph)))
flag = False
time = 25000
for r in result:
    if r!=-1:
        time = min(time, r)
        flag = True
print(time if flag else -1)