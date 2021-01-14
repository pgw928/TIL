import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

N, M = map(int, input().split())
graph = { i : [] for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [0] * N

def dfs(start_node, depth, N):
    print(f'node:{start_node}, detph:{depth}')
    node = start_node
    visited[node] = 1
    if depth == 4:
        print(f'result:{1}')
        return 1

    for n_node in graph[node]:
        if not visited[n_node]:
            visited[n_node] = 1
            result = dfs(n_node, depth+1, N)
            print('done')
            visited[n_node] = 0
            if result == 1:
                return result
    visited[node] = 0
    return 0


def sol():

    for node in range(N):
        if dfs(node, 0, N) == 1:
            print('---------------')
            return 1
    return 0
print(sol())



