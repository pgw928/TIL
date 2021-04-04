import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [-1, 1, 0 ,0], [0, 0, -1, 1]
visited = [[1]*n for _ in range(n)]
def bfs(s):
    dq, check = deque(), []
    dq.append(s)
    check.append(s)
    visited[s[0]][s[1]] = 0
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<n and 0<=a<n:
                if graph[b][a]==1 and visited[b][a]:
                    check.append((b,a))
                    visited[b][a] = 0
                    dq.append((b, a))
    return check

def count(tmp1, tmp2):
    m = float('inf')
    for (y, x) in tmp1:
        for (b, a) in tmp2:
            m = min(m, abs(b-y)+abs(x-a)-1)
    return m

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and visited[i][j]:
            tmp = bfs((i, j))
            result.append(tmp)

l, m = len(result), float('inf')
for i in range(l-1):
    for j in range(i+1, l):
        m = min(m, count(result[i],result[j]))
print(m)
