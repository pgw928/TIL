import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = {i:[] for i in range(1,n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

check = [-1]*(n+1)
def bfs(start):

    dq = deque()
    dq.append(start)
    check[start] = 0
    while dq:
        node = dq.popleft()
        for n_node in graph[node]:
            if check[n_node]==-1:
                check[n_node] = node
                dq.append(n_node)

bfs(1)

for i in range(2, n+1):
    print(check[i])