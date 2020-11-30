# 내 풀이
import sys
sys.setrecursionlimit(10**8)
N, K = map(int,sys.stdin.readline().split())
M = 10**5
graph = [-1] * (1+M)
graph[N]=0

from collections import deque
def bfs(start_node, end_node):
    dq = deque()
    dq.append(start_node)
    if start_node == end_node:
        return 0
    while dq:
        print(dq)
        node = dq.popleft()
        for k in [node-1, node+1 ,2*node]:
            if (0 <= k <= M) and (graph[k])==-1:
                dq.append(k)
                graph[k] = graph[node] + 1
            if graph[K]!=-1: # 오히려 이부분이 속도를 느리게 만든다..
                break
    return graph[K]


print(bfs(N, K))

# 다른 사람 풀이
# import sys
# from collections import deque
# sys.setrecursionlimit(10**8)
# N, K = map(int,sys.stdin.readline().split())
#
# MAX = 10 ** 5
# D = [-1] * (MAX+1)
# D[N] = 0
# dq = deque()
# dq.append(N)
# while dq:
#     node = dq.popleft()
#     for k in [node-1, node+1, 2*node]:
#         if 0<= k <= MAX and D[k]==-1:
#             dq.append(k)
#             D[k] = D[node]+1
#
# print(D[K])
