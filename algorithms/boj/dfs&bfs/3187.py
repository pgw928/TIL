import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline


R, C = map(int, input().split())
graph =[ list(input().strip()) for _ in range(R)]

print(graph)

visited = [[0] * C for _ in range(R)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(start_node):
    y, x = start_node

    if visited[y][x] == 1 or graph[y][x] == '#':
        return

    if graph[y][x] == 'v':
        visited[y][x] = 1
        wolf_and_sheep[0] += 1

    elif graph[y][x] == 'k':
        visited[y][x] = 1
        wolf_and_sheep[1] += 1
    elif graph[y][x] == '.':
        visited[y][x] = 1



    for k in range(4):
        yy = y + dy[k]
        xx = x + dx[k]

        if 0 <= yy < R and 0 <= xx < C:
            if visited[yy][xx] == 0 and graph[yy][xx] == 'v':
                dfs((yy, xx))

            elif visited[yy][xx] == 0 and graph[yy][xx] == 'k':
                dfs((yy, xx))

            elif visited[yy][xx] == 0 and graph[yy][xx] == '.':
                dfs((yy, xx))
    return


wolf = sheep = 0
for i in range(R):
    for j in range(C):
        print('i:', i, 'j:', j)
        wolf_and_sheep = [0, 0]
        dfs((i, j))
        if wolf_and_sheep[1] > wolf_and_sheep[0]:
            wolf_and_sheep[0] = 0
        else:
            wolf_and_sheep[1] = 0
        print(wolf_and_sheep[0], wolf_and_sheep[1])
        wolf += wolf_and_sheep[0]
        sheep += wolf_and_sheep[1]

print(sheep, wolf)

