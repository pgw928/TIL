import sys
import heapq
from math import inf

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())


visited = [False]*(n+1)
distance = [inf]*(n+1)

def dijkstra(start):
    q = []
    # 시작 노드에서 노드 까지 거리 : 0
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        # 가장 거리가 짧은 노드에 대한 정보 꺼내기
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue
        for n_node, n_dist in graph[node]:
            tmp = dist + n_dist
            if tmp < distance[n_node]:
                distance[n_node] = tmp
                heapq.heappush(q, (tmp, n_node))

dijkstra(start)

print(distance[end])