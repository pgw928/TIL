import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

def make_check(graph, i, N):

    new_graph = [[] for _ in range(N)]
    for n in range(N):
        for m in range(N):
            if graph[n][m] <= i:
                new_graph[n].append(1)
            else:
                new_graph[n].append(0)
    return new_graph



dy = [1, -1, 0, 0]
dx = [0, 0 ,1, -1]

def dfs(new_graph, start_node):

    y, x = start_node
    if new_graph[y][x] == 1:
        return False

    if new_graph[y][x] == 0:
        new_graph[y][x] = 1
        for k in range(4):
            b, a = (y+dy[k], x+dx[k])
            if a<0 or b<0 or a>=N or b>=N:
                continue
            if new_graph[b][a] == 0:
                dfs(new_graph, (b,a))
    return True

M = 0
for k in range(0, 99):
    new_graph = make_check(graph, k, N)
    ret = 0
    for i in range(N):
        for j in range(N):
            if dfs(new_graph, (i, j)):
                ret += 1
    M = max(ret, M)

print(M)