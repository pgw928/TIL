import sys

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

graph.sort(key=lambda x: (x[0], x[1]))

for g in graph:
    print(g[0], g[1])

