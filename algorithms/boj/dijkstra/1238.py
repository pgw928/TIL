import sys
import heapq
from math import inf

input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [ [] for i in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


distance = [inf]*(N+1)

def dijkstra(start_node):
    h = []
    heapq.heappush(h,(0, start_node))
    distance[start_node] = 0
    while h:
        dist, node = heapq.heappop(h)
        if dist < distance[node]:
            continue
        for n_node, n_dist in graph[node]:
            tmp = n_dist + dist
            if tmp < distance[n_node]:
                distance[n_node] = tmp
                heapq.heappush(h, (tmp, n_node))

result = [0]*(N+1)
for i in range(1,N+1):
    distance = [inf] * (N + 1)
    dijkstra(i)
    result[i] = distance[X]

print(result)
distance = [inf] * (N + 1)
dijkstra(X)

result = [ result[i] + distance[i]  for i in range(1, len(result))]
print(max(result))
