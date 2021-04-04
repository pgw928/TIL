import sys; input = sys.stdin.readline
from collections import deque

def classify(n, m, graph):
    fire = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                start = (i, j)
            elif graph[i][j] == '*':
                fire.append((i, j))
    return fire, start

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(fire, start):
    dq, visited = deque(), [[-1]*m for _ in range(n)]
    dq.append(start)
    visited[start[0]][start[1]] = 0
    cnt = 0
    while dq:
        y, x = dq.popleft()
        if graph[y][x]=='.' and (y==0 or y==n-1 or x==0 or x==m-1):
            return visited[y][x] + 1
        tmp = []
        if cnt == visited[y][x]:
            for i, j in fire:
                for k in range(4):
                    b, a = i+dy[k], j+dx[k]
                    if 0<=b<n and 0<=a<m and graph[b][a]=='.':
                        tmp.append((b, a))
                        graph[b][a] = '*'
            cnt += 1
            fire = tmp

        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0 <= b < n and 0 <= a < m and graph[b][a] == '.' and visited[b][a]==-1:
                dq.append((b, a))
                visited[b][a] = visited[y][x] + 1
    return 'IMPOSSIBLE'


for _ in range(int(input())):
    m, n = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]
    fire, start = classify(n, m, graph)
    graph[start[0]][start[1]] = '.'
    print(bfs(fire, start))