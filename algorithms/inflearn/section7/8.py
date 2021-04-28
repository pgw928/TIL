import sys
from collections import deque
sys.stdin = open('section7/input.txt', 'rt')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)] 
def bfs(start=(n//2, n//2)):
    res = 0
    dq = deque()
    dq.append(start)
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<n and 0<=a<n and (abs(b-n//2)+abs(a-n//2)<=n//2) and visited[b][a]==0:
                visited[b][a] = 1
                dq.append((b, a))
                res += graph[b][a]
    return res

print(bfs())
for v in visited:
    print(v)