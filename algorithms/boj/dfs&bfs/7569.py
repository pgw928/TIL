import sys
sys.setrecursionlimit(10000)
M, N , H = map(int, sys.stdin.readline().split())
graph = []
for _ in range(H):
    temp = []
    for _ in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
    graph.append(temp)

pt = [[h,n,m] for h in range(H) for n in range(N) for m in range(M) if graph[h][n][m]==1]

from collections import deque
def bfs(start_nodes):
    dq = deque()
    dq.extend(start_nodes)

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while dq:
        node = dq.popleft()
        x = node[0]
        y = node[1]
        z = node[2]
        for i in range(6):
            a = x+dx[i]
            b = y+dy[i]
            c = z+dz[i]
            if a<0 or b<0 or c<0 or a>=H or b>=N or c>=M:
                continue
            if graph[a][b][c]==0:
                graph[a][b][c] = graph[x][y][z] + 1
                dq.append([a, b, c])
print(graph)
bfs(pt)
def result():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m]==0:
                    return False
    return True

if max(max(max(graph))) == -1:
    print(-1)
elif not result():
    print(-1)
else:
    print(max(max(max(graph))) - 1)





