import sys
from collections import deque

input = sys.stdin.readline

N  = int(input())

r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]
visited = [[0]*N for _ in range(N)]

def bfs(start_node, end_node):

    dq = deque()
    dq.append(start_node)
    visited[start_node[0]][start_node[1]] = 1
    while dq:
        print(dq)
        node = dq.popleft()
        if node == end_node:
            return visited[end_node[0]][end_node[1]]-1
        x, y = node
        for ddx, ddy in zip(dx, dy):
            a, b = (ddx+ x, ddy + y)
            if (0 <= a < N) and (0 <= b < N):
                if visited[a][b] == 0:
                    visited[a][b] = visited[x][y] + 1
                    dq.append((a,b))
    return -1
print(bfs((r1,c1), (r2,c2)))






