import sys; input = sys.stdin.readline
from collections import deque
t = int(input())

def bfs(a, b):
    dq  = deque()
    dq.append((a, ''))
    visited[a] = 1
    while dq:
        x, res = dq.popleft()
        if x==b:
            return res
        tmp1 = 2*x if 2*x<10000 else (2*x)%10000
        if visited[tmp1]==0:
            dq.append((tmp1, res+'D'))
            visited[tmp1] = 1
        tmp2 = x -1 if x!=0 else 9999
        if visited[tmp2]==0:
            dq.append((tmp2, res+'S'))
            visited[tmp2]=1

        x_str = '0'*(4-len(str(x))) +str(x)
        tmp3 = int(x_str[1:] + x_str[0])
        if visited[tmp3]==0:
            dq.append((tmp3, res+'L'))
            visited[tmp3]=1
        tmp4 = int(x_str[-1]+x_str[:3])
        if visited[tmp4]==0:
            dq.append((tmp4, res+'R'))
            visited[tmp4]=1

for _ in range(t):
    a, b = map(int, input().split())
    visited = [0]*10000
    print(bfs(a, b))