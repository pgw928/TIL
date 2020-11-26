import sys

N, M= map(int,sys.stdin.readline().split())
#
graph = []
for i in range(N):
    graph.append(list(map(int,list(sys.stdin.readline().strip()))))

print(N, M)
print(graph)
# lst = list(map(int,list(sys.stdin.readline().strip())))
from collections import deque

def bfs(graph, start_node):
    dq = deque()
    dq.append(start_node)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1 ,1]

    while dq:
        x, y = dq.popleft()
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a <=-1 or a>=N or b<=-1 or b>=M :
                continue
            if graph[a][b]==0:
                continue
            if graph[a][b]==1:
                graph[a][b]= graph[x][y]+1
                dq.append((a,b))
                print('a : {}, b : {}'.format(a, b), graph[a][b])
            print(dq, graph[a][b])
    return graph[N-1][M-1]


print(bfs(graph,(0,0)))
