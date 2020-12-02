import sys
sys.setrecursionlimit(10000)

def dfs(start_node):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x = start_node[0]
    y = start_node[1]
    if x <= -1 or y <= -1 or x >= M or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs((x - 1, y))
        dfs((x + 1, y))
        dfs((x, y - 1))
        dfs((x, y + 1))
        return True
    return False

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    print('M : {}, N : {}, K : {}'.format(M, N ,K))
    graph = [ [] for _ in range(M) ]
    for i in range(M):
        for _ in range(N):
            graph[i].append(0)

    for s in range(K):
        i, j = map(int, sys.stdin.readline().split())
        print('i : {}, j : {}'.format(i, j))
        graph[i][j] = 1


    result = 0
    for i in range(M):
        for j in range(N):
            if dfs((i,j)):
                result += 1
    print(result)