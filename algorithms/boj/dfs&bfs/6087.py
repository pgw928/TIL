import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = [list(input()) for _ in range(N)]
nodes = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'C':
            nodes.append((i,j))

start_node = nodes[0]
end_node = nodes[1]

check = [[-1]*M for _ in range(N)]
result = [[0]*M for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(start_node, end_node):

    dq = deque()
    dq.append(start_node)
    check[start_node[0]][start_node[1]] = 4

    while dq:
        y, x = dq.popleft()
        if (y,x) == end_node:

            return result[end_node[0]][end_node[1]]

        for k in range(4):
            b , a = y + dy[k] , x + dx[k]

            if (0<=b<=N-1) and (0<=a<=M-1) and (check[b][a] == -1) and (graph[b][a]=='.'):
                if check[y][x] != k:
                    result[b][a] = result[y][x]+1

                else:
                    result[b][a] = result[y][x]
                check[b][a] = k
                print('result:', result[b][a])
                dq.append((b,a))
    return result[end_node[0]][end_node[1]]


print(bfs(start_node, end_node))
print(result)
print(check)
