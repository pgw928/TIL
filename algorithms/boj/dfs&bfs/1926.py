import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [ list(map(int, input().split())) for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(start_node):
    global result
    y, x = start_node
    if graph[y][x]==0:
        return
    graph[y][x] = 0
    result += 1


    for k in range(4):
        b = y + dy[k]
        a = x + dx[k]
        if (0<=b<n) and (0<=a<m) and (graph[b][a]==1):
            dfs((b,a))


count = 0
result = 0
M = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            count += 1
            dfs((i,j))
            M = max(result, M)
            result = 0
print(count)
print(M)