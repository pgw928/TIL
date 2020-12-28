import sys

input = sys.stdin.readline

N, M = map(int, input().split())
print(N, M)
graph =[ list(map(int, input().split())) for _ in range(N)]
print(graph)
dy = [-1, 1, 0, 0]
dx = [0 ,0 ,-1, 1]

def dfs(start_node):

    y, x = start_node

    for i in range(4):
        b = y + dy[i]
        a = x + dx[i]
        print(check, a,b)
        if a<0 or b<0 or b>N or a>M:
            continue
        if check[b][a] != 0:
            continue
        check[b][a] = 1 + check[y][x]
        adding = dfs((b,a))
        print(check)
        if check[b][a] == 3:
            return graph[b][a]
    return graph[b][a] + adding

print(dfs((0,0)))