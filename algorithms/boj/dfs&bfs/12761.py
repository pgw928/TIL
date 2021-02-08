import sys
from collections import deque
input = sys.stdin.readline

a, b, start, end = map(int, input().split())

def bfs(start, end):
    dq, check = deque(), set()
    dq.append(start)
    check.add(start[0])
    while dq:
        node, s = dq.popleft()
        if node == end:
            return s
        for n_node in [node-1, node+1, node+a, node-a, node*a, node+b, node-b, node*b]:
            if n_node not in check and 0<=n_node<=100000:
                check.add(n_node)
                dq.append((n_node, s+1))

print(bfs((start,0),end))
