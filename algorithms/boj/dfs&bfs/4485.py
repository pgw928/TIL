import sys; input = sys.stdin.readline
from collections import deque
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(node=(0, 0)):
    dq = deque()
    dq.append(node)
    dp[node[0]][node[1]] = graph[node[0]][node[1]]
    while dq:
        y, x = dq.popleft()
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<n and 0<=a<n and dp[y][x] + graph[b][a] < dp[b][a]:
                dp[b][a] = dp[y][x] + graph[b][a]
                dq.append((b,a))

j = 1
while True:
    n = int(input())
    if n==0:
        break
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
    dp = [[float('inf')]*n for _ in range(n)]
    bfs()
    print(f'Problem {j}: {dp[-1][-1]}')
    j += 1