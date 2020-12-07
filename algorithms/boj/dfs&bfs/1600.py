import sys

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split())

graph = []
for _ in range(H):
    graph.append(list(map(int, sys.stdin.readline().split())))

print(K,W,H,graph)

mapping = [[0]*W for _ in range(H)]

from collections import deque

dy_k = [2, 2, 1, -1, 1, -1, 0, 0]
dx_k = [1, -1, 2, 2, 0, 0, 1, -1]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(K, start_node=(0,0)):


