import sys
import heapq
from math import inf
from itertools import combinations


input = sys.stdin.readline
N, M, K = map(int, input().split())


pre = [tuple(map(int, input().split())) for _ in range(M)]
combs = combinations(range(M),K)


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, node  = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        for n_node, n_dist in graph[node]:
            tmp = n_dist + distance[node]
            if tmp < distance[n_node]:
                distance[n_node] = tmp
                heapq.heappush(hq, (tmp, n_node))

m = inf
for A in combs:
    distance = [inf] * (N + 1)
    graph = [[] for _ in range(M + 1)]
    for i in range(M):
        a, b, c = pre[i]
        if i in A:
            graph[a].append((b,0))
            graph[b].append((a,0))
        else:
            graph[a].append((b,c))
            graph[b].append((a,c))
    dijkstra(1)
    m = min(m, distance[N])

print(m)