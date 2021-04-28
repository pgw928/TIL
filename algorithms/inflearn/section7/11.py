import sys
sys.stdin = open('section7/input.txt', 'rt')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
inf, sup = float('inf'), - float('inf')

for i in range(n):
    for j in range(n):
        if graph[i][j] > sup:
            end = (i, j)
            sup = graph[i][j]
        if graph[i][j] < inf:
            start = (i, j)
            print(i,j, graph[i][j])
            inf = graph[i][j]
print(start, end)

cnt = 0
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(node=start):
    global cnt
    if node==end:
        cnt += 1
        return
    y, x = node 
    for k in range(4):
        b, a = y+dy[k], x+dx[k]
        if 0<=b<n and 0<=a<n and graph[b][a]>graph[y][x] and visited[b][a]== 0:
            visited[b][a] = 1
            dfs((b, a))
            visited[b][a] = 0
visited[0][0] = 1
dfs()
print(cnt)