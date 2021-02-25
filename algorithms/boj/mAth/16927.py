import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
h = n//2
w = m//2
def sol():
    for k in range(min(h,w)):
        tmp1, tmp2 = graph[k][k], graph[n-1-k][m-1-k]
        for i in range(n-2*k-1):
            tmp1, graph[i+k+1][k] = graph[k+i+1][k], tmp1
            tmp2, graph[-i - 2 - k][m - 1 - k] = graph[-i - 2 - k][m - 1 - k], tmp2

        for i in range(m-2*k-1):
            tmp1, graph[n-1-k][i+k+1] = graph[n-1-k][i+k+1], tmp1
            tmp2, graph[k][-i + m - 2 - k] = graph[k][-i + m - 2 - k], tmp2


for _ in range(r):
    sol()

for g in graph:
    print(' '.join(tuple(map(str, g))))