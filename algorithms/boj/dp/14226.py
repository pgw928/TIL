import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
visited = [[-1]*(2000+1) for _ in range(2000+1)]

def bfs(start = 1):
    dq = deque()
    dq.append((start, 0))
    visited[start][0] = 0
    while dq:
        x, c = dq.popleft()
        if x==n:
            return min([a for a in visited[n] if a>-1])
        if visited[x][x]==-1:
            visited[x][x] = visited[x][c] + 1
            dq.append((x, x))
        if 0<=x+c<=2000 and visited[x+c][c]==-1:
            visited[x+c][c] = visited[x][c] + 1
            dq.append((x+c, c))
        if x-1>=0 and visited[x-1][c]==-1:
            visited[x-1][c] = visited[x][c] + 1
            dq.append((x-1, c))
print(bfs())