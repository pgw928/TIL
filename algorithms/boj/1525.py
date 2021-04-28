import sys; input = sys.stdin.readline
from collections import deque
puzzle = [list(map(int, input().split())) for _ in range(3)]
bk_pt = False
for i in range(3):
    for j in range(3):
        if puzzle[i][j]==0:
            start = (i, j)
            bk_pt = True
            break
    if bk_pt:
        break

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(node):
    dq = deque()
    dq.append(node)
    while dq:
        y, x = dq.popleft()
