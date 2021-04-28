import sys; input= sys.stdin.readline
from collections import deque
n, t, g = map(int, input().split())
M = 99_999
def bfs(n):
    dq, visited = deque(), [-1]*(M+1)
    dq.append(n)
    visited[n] = 0
    while dq:
        x = dq.popleft()
        if visited[x] > t:
            continue
        if x==g:
            return visited[g]

        y = x+1
        if y<=M and visited[y]==-1:
            dq.append(y)
            visited[y] = visited[x] + 1
        y = 2*x
        if y>M:
            continue
        y -= 10**(len(str(y))-1)
        if y>=0 and  visited[y] == -1:
            dq.append(y)
            visited[y] = visited[x] + 1

    return 'ANG'

print(bfs(n))