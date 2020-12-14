import sys

sys.setrecursionlimit(8000)

input = sys.stdin.readline

N, M = map(int, input().split())


graph = [list(map(int, input().split()))  for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(start_node) :

    x, y = start_node
    if x < 0 or y < 0 or x > N or y > M:
        return 0
    if s[x][y]!=1:
        return 0
    if graph[x][y]!=0 and s[x][y]==1:
        count = 0
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a < 0 or b < 0 or a > N or b > M:
                continue
            if graph[a][b]==0 and s[a][b]==0:
                count += 1
        s[x][y] = -1
        graph[x][y] = max(0, graph[x][y]-count)
        dfs((x - 1, y))
        dfs((x + 1, y))
        dfs((x, y - 1))
        dfs((x, y + 1))
        return 1
    return 0

result = 0
breakpt1 = False
breakpt2 = False
zeros = [ [0]*M for _ in range(N)]

while True:
    s = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                s[i][j] = 1
    stop = 0
    for i in range(N):
        for j in range(M):
            if s[i][j]==1:
                stop += 1
                result += 1
                if stop==2 or graph==zeros:
                    breakpt1 = True
                    break
                dfs((i,j))
                print('------------')
                print(graph, stop)
                print('------------')
        if breakpt1:
            breakpt2 =True

    if breakpt2:
        break
print(result-stop)