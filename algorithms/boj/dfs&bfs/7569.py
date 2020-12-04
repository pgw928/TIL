import sys

sys.setrecursionlimit(8000)
M, N, H = map(int, sys.stdin.readline().split())
graph = []
for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
    graph.append(temp)

pt = [(h, n, m) for h in range(H) for n in range(N) for m in range(M) if graph[h][n][m] == 1]

from collections import deque


def bfs(start_nodes):
    dq = deque()
    dq.extend(start_nodes)

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while dq:
        x, y, z = dq.popleft()
        for i in range(6):
            a = x + dx[i]
            b = y + dy[i]
            c = z + dz[i]
            if a < 0 or b < 0 or c < 0 or a >= H or b >= N or c >= M:
                continue
            if graph[a][b][c] == 0:
                graph[a][b][c] = graph[x][y][z] + 1
                dq.append([a, b, c])


bfs(pt)


def result():
    ans = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] == 0:
                    return -1
                ans = max(ans, graph[h][n][m])
    return ans


cnt = result()
print(-1 if cnt == -1 else cnt - 1)





