import sys
from collections import deque
sys.stdin = open('section7/input.txt', 'rt')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [-1, 1, 0, 0, 1, 1, -1, -1], [0, 0, -1, 1, 1, -1, 1, -1]
def bfs(node):
    dq = deque()
    dq.append(node)
    graph[node[0]][node[1]] = 0
    while dq:
        y, x = dq.popleft()
        for k in range(8):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<n and 0<=a<n and graph[b][a]==1:
                graph[b][a] = 0
                dq.append((b,a))

cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bfs((i,j))
            cnt += 1
            
print(cnt)