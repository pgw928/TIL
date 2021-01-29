import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split()))  for _ in range(N)]

check = [ [-1]*M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, current, nodes):

    y, x = start
    count = 0
    for k in range(4):
        b, a = (y + dy[k], x + dx[k])
        if (0 <= b <= N - 1) and (0 <= a <= M - 1) and (graph[b][a]==0):
            count += 1

    dq = deque()
    dq.append((y,x,count))
    check[start[0]][start[1]] = current
    nodes.remove((y, x))
    while dq:
        y, x, c = dq.popleft()

        for k in range(4):
            b, a = (y+dy[k], x+dx[k])
            count = 0
            if (0<=b<=N-1) and (0<=a<=M-1):
                for i in range(4):
                    u, v = b+dy[i], a+dx[i]
                    if (0 <= u <= N - 1) and (0 <= v <= M - 1) and (graph[u][v] == 0):
                        count += 1

                if (check[b][a]==current-1) and (graph[b][a]!=0):
                    dq.append((b, a, count))
                    nodes.remove((b, a))
                    check[b][a] += 1
        graph[y][x] = max(graph[y][x]-c, 0)


def sol():

    current = 0
    while True:
        nodes = [(i,j) for i in range(N) for j in range(M) if graph[i][j]!=0]
        if not nodes:
            return 0

        bfs(nodes[0], current, nodes)
        current += 1
        if nodes:
            return current-1

print(sol())