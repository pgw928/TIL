import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

m, n, k = map(int, input().split())

graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        for i in range(y1, y2):
            if graph[i][j]==0:
                graph[i][j] = 1

dy, dx = [0, 0, -1, 1], [1, -1, 0, 0]
def dfs(start):
    global size
    y, x = start
    graph[y][x] = 1
    size += 1
    for i in range(4):
        b, a = y+dy[i], x+dx[i]
        if 0<=b<=m-1 and 0<=a<=n-1 and graph[b][a]==0:
            dfs((b,a))



count = 0
result = []
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            size = 0
            count += 1
            dfs((i,j))
            result.append(size)

print(count)
print(' '.join(list(map(str, sorted(result)))))