import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
# visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
zeros = [ (i, j)  for i in range(N) for j in range(M) if graph[i][j]==0]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(start_node):


    y, x = start_node
    if (visited[y][x] == 1) or (graph[y][x] == 0):
        return 0


    dq = deque()
    dq.append(start_node)
    visited[y][x] = 1
    count = 1

    while dq:
        # print(dq)
        y, x = dq.popleft()
        for k in range(4):
            b, a = (y+dy[k], x+dx[k])
            if 0<=a<=M-1 and 0<=b<=N-1:
                if (visited[b][a]==0) and (graph[b][a]==1):
                    visited[b][a]= 1
                    count +=1
                    dq.append((b,a))
    return count

MA = 1
for u, v in zeros:
    graph[u][v] = 1
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            result = bfs((i,j))
            MA = max(result, MA)
    graph[u][v] = 0
print(MA)