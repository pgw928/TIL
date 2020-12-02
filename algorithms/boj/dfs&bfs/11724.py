import sys

# ---------INPUT---------
N, M = map(int,sys.stdin.readline().split())

temp = []
for _ in range(M):
    temp.append(list(map(int,sys.stdin.readline().split())))

graph = { j:[] for j in range(1,N+1)}

for j in range(M):
    u = temp[j][0]
    v = temp[j][1]
    graph[u].append(v)
    graph[v].append(u)

check = [0]*(N+1)
# -----------------------

from collections import deque
def bfs(start_node):

    dq = deque()
    dq.append(start_node)
    while dq:
        node = dq.popleft()
        if check[node]==0 :
            check[node]=1
            dq.extend(graph[node])
    return 1

result = 0
for j in range(1,N+1):
    if check[j]==0:
      result += bfs(j)

print(result)