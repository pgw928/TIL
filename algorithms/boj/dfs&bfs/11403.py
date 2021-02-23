import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(start):
    check = [False]*n
    dq = deque()
    dq.append(start)

    while dq:
        node = dq.popleft()
        for n_n in [idx for idx, k in enumerate(graph[node]) if k==1]:
            if not check[n_n] and graph[node][n_n]==1:
                dq.append(n_n)
                graph[start][n_n] = 1
                check[n_n] = True


for i in range(n):
    bfs(i)
for g in graph:
    print(' '.join(map(str, g)))