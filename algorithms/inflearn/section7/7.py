import sys
from collections import deque
# sys.stdin = open('section7/input.txt', 'rt')
# s, e = map(int, input().split())
s, e = 7, 8945
check = [-1]*(10_000+1)
def bfs(node):
    dq = deque()
    dq.append(node)
    check[node] = 0
    while dq:
        x = dq.popleft()
        if x==e:
            return check[x]
        for y in [x+5, x-1, x+1]:
            if 1<=y<=10000 and check[y]==-1:
                dq.append(y)
                check[y] = check[x] + 1

print(bfs(s))    