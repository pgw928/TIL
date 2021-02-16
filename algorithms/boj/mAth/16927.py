import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

h = n//2
w = m//2
print(h, w)
def sol(graph, k):
    tmp = graph[k][k]
    for i in range(n-2*k-1):
        tmp, graph[i+k+1][k] = graph[k+i+1][k], tmp

    for i in range(m-2*k-1):
        tmp, graph[n-1-k][i+k+1] = graph[n-1-k][i+k+1], tmp

    for i in range(n-2*k-1):
        tmp, graph[-i-2-k][m-1-k] = graph[-i-2-k][m-1-k], tmp

    for i in range(m-2*k-1):
        tmp, graph[k][-i+m-2-k] = graph[k][-i+m-2-k], tmp

for _ in range(r):
    for k in range(min(h,w)):
        sol(graph, k)

for g in graph:
    print(' '.join(tuple(map(str, g))))