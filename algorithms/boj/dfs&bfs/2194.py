import sys
from collections import deque
input = sys.stdin.readline
n,m , a,b , k = map(int, input().split())
obstacles = {tuple(map(int, input().split())) for _ in range(k)}
(s1, s2), (e1, e2) = map(int, input().split()), map(int, input().split())

dy, dx = [1,-1, 0, 0], [0, 0, -1, 1]
def bfs(start):

    dq, check = deque(), set()
    check.add(start)
    dq.append((start[0],start[1],0))
    while dq:
        y, x, s = dq.popleft()
        if (y, x) == (e1, e2):
            return s
        for i in range(4):
            yy, xx = y+dy[i], x+dx[i]

            if (yy<1) or (yy>=n-a+2) or (xx<1) or (xx>=m-b+2) or ((yy, xx) in check):
                continue
            continue_pt = False
            if i==0:
                for j in range(xx, xx+b):
                    if (yy+a-1, j) in obstacles:
                        continue_pt = True
                        break
            elif i==1:
                for j in range(xx, xx+b):
                    if (yy, j) in obstacles:
                        continue_pt = True
                        break

            elif i==2:
                for j in range(yy, yy+a):
                    if (j, xx) in obstacles:
                        continue_pt = True
                        break
            elif i==3:
                for j in range(yy, yy+a):
                    if (j, xx+b-1) in obstacles:
                        continue_pt = True
                        break

            if continue_pt:
                continue
            dq.append((yy,xx, s+1))
            check.add((yy,xx))
    return -1
print(bfs((s1, s2)))
