import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
coins = tuple()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'o':
            coins += (i, j)
            graph[i][j] = '.'
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(coins):
    dq = deque()
    check = set()
    dq.append(coins+(0,))
    check.add(coins)
    while dq:
        y1, x1, y2, x2, c = dq.popleft()
        if c>9:
            continue
        for k in range(4):
            b1, a1 = y1+dy[k], x1+dx[k]
            b2, a2 = y2+dy[k], x2+dx[k]
            if b1==b2 and a1==a2:
                continue
            flag1 = b1<0 or b1>=n or a1<0 or a1>=m
            flag2 = b2<0 or b2>=n or a2<0 or a2>=m
            if (flag1 and not flag2) or (flag2 and not flag1):
                return c+1
            if flag1 and flag2:
                continue
            if graph[b1][a1]=='#':
                b1, a1 = y1, x1
            if graph[b2][a2]=='#':
                b2, a2 = y2, x2
            print(b1, a1, b2, a2)

            if (b1, a1, b2, a2) not in check:
                dq.append((b1, a1, b2, a2, c+1))
                check.add((b1, a1, b2, a2))
    return -1
print(bfs(coins))