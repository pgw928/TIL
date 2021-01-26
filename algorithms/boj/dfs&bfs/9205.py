import sys
from collections import deque
input = sys.stdin.readline


t = int(input().strip())

def bfs(start, end):

    dq = deque()
    dq.append(start)

    while dq:
        x, y = dq.popleft()
        if (abs(end[0]-x)+abs(end[1]-y)) <= 1000:
            return 'happy'

        for k in range(0, n+1):
            a, b = coords[k]
            if (check[k] == 0) and ((abs(a-x)+abs(b-y))<=1000):
                dq.append(coords[k])
                check[k] = 1
    return 'sad'

for _ in range(t):
    n = int(input().strip())

    start = tuple(map(int, input().strip().split()))
    coords = [tuple(map(int, input().strip().split())) for _ in range(n + 1)]
    end = coords[-1]
    check = [0]*(n+2)
    print(bfs(start, end))