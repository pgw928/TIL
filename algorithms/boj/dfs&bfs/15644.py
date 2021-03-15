import sys; input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]=='R':
            graph[i][j] = '.'
            red = (i, j)
        elif graph[i][j]=='B':
            blue = (i, j)
            graph[i][j] = '.'
        elif graph[i][j]=='O':
            hole = (i, j)

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
state = ['D', 'U', 'R', 'L' ]
def bfs(red, blue):
    dq, check = deque(), set()
    dq.append((red[0], red[1], blue[0], blue[1], 0, ''))
    check.add((red[0], red[1], blue[0], blue[1]))
    while dq:
        r_y, r_x, b_y, b_x, count , direct = dq.popleft()
        for k in range(4):
            r_yy, r_xx, b_yy, b_xx = r_y, r_x, b_y, b_x
            ct_pt = False
            r_count , b_count = 0, 0
            while True:
                if graph[r_yy][r_xx]=='.':
                    r_yy += dy[k]
                    r_xx += dx[k]
                    r_count += 1
                if graph[b_yy][b_xx] == '.':
                    b_yy += dy[k]
                    b_xx += dx[k]
                    b_count += 1
                elif graph[b_yy][b_xx]=='O':
                    ct_pt = True
                    break
                if (graph[r_yy][r_xx]=='#' or graph[r_yy][r_xx]=='O') and graph[b_yy][b_xx]=='#':
                    break
            if ct_pt:
                continue
            if graph[r_yy][r_xx]=='O':
                return count+1, direct+state[k]
            r_yy -= dy[k]
            r_xx -= dx[k]
            b_yy -= dy[k]
            b_xx -= dx[k]
            if (r_yy, r_xx)==(b_yy, b_xx):
                if b_count > r_count:
                    b_yy -= dy[k]
                    b_xx -= dx[k]
                else:
                    r_yy -= dy[k]
                    r_xx -= dx[k]
            if count <9 and ((r_yy, r_xx, b_yy, b_xx) not in check):
                dq.append((r_yy, r_xx, b_yy, b_xx, count+1, direct+state[k]))
                check.add((r_yy, r_xx, b_yy, b_xx))
    return [-1]

result = bfs(red, blue)
if len(result)==1:
    print(-1)
else:
    print(result[0])
    print(result[1])