import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int ,input().split())
bam = dict()
for _ in range(n+m):
    x, y = map(int, input().split())
    bam[x] = y

def bfs():
    dq, visited =  deque(), [float('inf')]*101
    visited[1] = 0
    dq.append(1)
    while dq:
        x = dq.popleft()
        if x==100:
            return visited[x]
        for k in range(1, 7):
            y = x + k
            if y <= 100:
                if y in bam and visited[y]>visited[x]+1:
                    dq.append(bam[y])
                    visited[y] = visited[x] + 1
                    visited[bam[y]] = visited[x] + 1
                elif visited[y]>visited[x]+1:
                    dq.append(y)
                    visited[y] = visited[x] + 1
print(bfs())