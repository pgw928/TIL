import sys; input = sys.stdin.readline
from collections import deque
n, k = map(int, input().split())
M = 500_000
odd_visited, even_visited = [0]*(M+1), [0]*(M+1)
def bfs(start, end):
    dq = deque()
    dq.append((start, end, 0, 0))
    even_visited[start] = 1
    even_odd = [0]*2
    m = M
    while dq:
        x, y, dy, cnt = dq.popleft()
        if x==y:
            even_odd[cnt % 2] = 1
            m = min(m, cnt)

        dy += 1
        y += dy

        if y>M:continue
        cnt += 1
        if cnt%2==0:
            if even_visited[y]==1:
                even_odd[0] = 1
                m = min(m, cnt)
            for z in [x-1, x+1, 2*x]:
                if 0 <= z <= M and even_visited[z]==0:
                    dq.append((z, y, dy, cnt))
                    even_visited[z] = 1
        elif cnt%2==1:
            if odd_visited[y]==1:
                even_odd[1] = 1
                m = min(m, cnt)
            for z in [x-1, x+1, 2*x]:
                if 0 <= z <= M and odd_visited[z]==0:
                    dq.append((z, y, dy, cnt))
                    odd_visited[z] = 1
        if sum(even_odd) == 2:
            return m
    if sum(even_odd) == 0:
        return -1
    return m

print(bfs(n, k))