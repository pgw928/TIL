import sys
import heapq
from math import inf

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())


graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, node = heapq.heappop(hq)

        if distance[node] < dist:
            continue

        for n_node, n_dist in graph[node]:
            tmp = n_dist + dist
            if tmp < distance[n_node]:
                distance[n_node] = tmp
                heapq.heappush(hq, (tmp, n_node))


distance = [inf]*(V+1)
dijkstra(K)
for d in distance[1:]:
    print('INF' if d==inf else d)
