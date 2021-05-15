import sys; input = sys.stdin.readline
n, m = map(int, input().split())
visited = [[0]*m for _ in range(n)]
k = int(input())
for _ in range(k):
    i, j = map(int, input().split())
    visited[i][j] = 1
y, x = map(int, input().split())
visited[y][x] = 1
direction = tuple(map(int, input().split()))
dy, dx = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]

idx = 0
l = len(direction)

while True:
    d = direction[idx]
    b, a = dy[d]+y, dx[d]+x
    if 0<=b<n and 0<=a<m and visited[b][a] == 0 :
        visited[b][a] = 1
        y, x = b, a
    else:
        visited[y][x] += 1
        if idx==l-1:
            idx = 0
        else:
            idx += 1
    if visited[y][x] == 5:
        break
print(y, x)