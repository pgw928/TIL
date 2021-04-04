import sys; input = sys.stdin.readline
from collections import deque
n, m = int(input()), int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
candi = [a-1 for a in  list(map(int, input().split()))]
s = candi[0]

def bfs(s):
    dq, check = deque(), set()
    dq.append(s)
    check.add(s)
    while dq:
        x = dq.popleft()
        for idx, y in enumerate(graph[x]):
            if y==1 and idx not in check:
                check.add(idx)
                dq.append(idx)
    if  set(candi) <= check:
        return 'YES'
    return 'NO'
print(bfs(s))