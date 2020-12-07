import sys

sys.setrecursionlimit(8000)

N, M = map(int, sys.stdin.readline().split())


graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
zeros = [ [0]*M for _ in range(N)]
s = [ [0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j]!=0:
            s[i][j] = 1


def dfs(start_node, k) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = start_node
    if x<0 or y<0 or x>N or y>M:
        return 0
    if s[x][y]!=k:
        return 0
    if graph[x][y]!=0:
        count = 0
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a < 0 or b < 0 or a > N or b > M:
                continue
            if graph[a][b]==0 and s[a][b]<=k:
                count += 1

        graph[x][y] = max(0, graph[x][y]-count)
        s[x][y] += 1
        dfs((x - 1, y), k)
        dfs((x + 1, y), k)
        dfs((x, y - 1), k)
        dfs((x, y + 1), k)
        return 1
    return 0


def sol():
    k = 0
    dct = {}
    print(graph)
    while True:
        if graph==zeros:
            return 0
        dct[k]= 0
        for i in range(N):
            for j in range(M):
                if graph[i][j]==0:
                    continue
                if s[i][j]>k+1:
                    continue
                dct[k] += dfs((i,j),k+1)
                if dct[k]>1:
                    return len(dct)-1
        print(graph)
        k += 1
print(sol())
