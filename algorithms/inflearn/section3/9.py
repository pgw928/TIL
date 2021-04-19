import sys
from collections import deque
sys.stdin = open('section3/input.txt', 'rt')
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def check(node=(0,0)):
    dq = deque()
    dq.append(node)
    visited[0][0] = 1
    cnt = 0
    while dq:
        flag = 1
        y, x = dq.popleft()            
        for k in range(4):
            b, a = dy[k]+y, dx[k]+x
            if 0<=b<n and 0<=a<n:
                if visited[b][a]==0:
                    dq.append((b, a))
                    visited[b][a] = 1
                if graph[y][x] <= graph[b][a]:
                    flag = 0
        cnt += flag
    return cnt

print(check())