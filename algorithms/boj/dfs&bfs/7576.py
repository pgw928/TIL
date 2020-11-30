import sys

N, M = map(int,sys.stdin.readline().split())
graph = []
for _ in range(M):
    graph.append(list(map(int,sys.stdin.readline().split())))

# print(graph)

from collections import deque
def bfs(start_nodes):
    dq = deque()
    dq.extend(start_nodes)
    count = 0
    while dq:
        for j in range(len(dq)):
            x,y = dq.popleft()
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for k in range(4):
                a = x + dx[k]
                b = y + dy[k]
                if a<0 or b<0 or a>=M or b>=N:
                    continue
                elif graph[a][b]==-1:
                    continue
                elif graph[a][b]==0:
                    graph[a][b]=1
                    dq.append((a,b))
        count+=1
    return count-1

start_nodes = []
for i in range(M):
    for j in range(N):
        if graph[i][j]==1:
            start_nodes.append((i,j))

result=bfs(start_nodes)

flag = 0
for i in range(M):
    for j in range(N):
        if graph[i][j]==0:
            flag = 1
if flag == 0:
    print(result)
else:
    print(-1)

