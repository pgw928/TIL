import sys
sys.setrecursionlimit(8000)
n, m = map(int, sys.stdin.readline().split())

graph= []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))


def dfs(start_node):
    x, y = start_node
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return 0
    if graph[x][y] == 0:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = 0

        s1 = dfs((x - 1, y))
        s2 = dfs((x + 1, y))
        s3 = dfs((x, y - 1))
        s4 = dfs((x, y + 1))
        s = (s1 + s2 + s3 + s4)
        return 1+s

count = 0
y= 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            y = max(y,dfs((i,j)))
            count += 1

print(count)
print(y)
