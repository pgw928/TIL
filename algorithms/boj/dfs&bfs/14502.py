# 연구소

import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]



def select_wall(graph):
    result = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                result.append((i, j))
    return combinations(result,3)

def count_zero(graph):
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                count += 1
    return count



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_node, new_graph, cand):
    dq = deque()
    dq.append(start_node)
    while dq:
        x, y = dq.popleft()
        if new_graph[x][y] == 2:
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if (0<=a<N) and (0<=b<M):
                    if new_graph[a][b] == 0:
                        new_graph[a][b] = 2
                        dq.append((a,b))
    return True

result = []
for cand in select_wall(graph):
    new_graph = deepcopy(graph)
    for u, v in cand:
        new_graph[u][v] = 1
    for i in range(N):
        for j in range(M):
            bfs((i,j), new_graph, cand)
    s = count_zero(new_graph)
    result.append(s)

print(max(result))


