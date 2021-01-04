import sys
from collections import deque

sys.setrecursionlimit(8000)

input = sys.stdin.readline
T = int(input())

start_node = 1

def bfs(start_node, N):
    dq = deque()
    dq.append(start_node)
    visited = [-1]* N
    # visited[1%N] = 0
    while dq:
        node = dq.popleft()
        if node%N == 0:
            print(visited)
            return node

        for i in [0, 1]:
            n_node = node * 10 + i
            if visited[n_node%N] == -1:
                visited[n_node%N] = n_node
                print(visited)
                dq.append(n_node)

for _ in range(T):
    print(bfs(start_node,int(input())))