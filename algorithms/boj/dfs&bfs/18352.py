import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = { i : [] for i in range(1,N+1)}

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
print(graph)
check = [-1]*(N+1)

def bfs(start_node, K):
    dq = deque()
    dq.append(start_node)
    check[start_node] = 1
    while dq:
        node = dq.popleft()
        for n_node in graph[node]:
            if check[n_node] == -1:
                check[n_node] = check[node] + 1
                dq.append(n_node)
    result = []
    for i in range(1,N+1):
        if check[i] == K+1:
            result.append(i)
    return result


result = bfs(X, K)
result.sort()
if result == []:
    print(-1)
else:
    for n in result:
        print(n)
