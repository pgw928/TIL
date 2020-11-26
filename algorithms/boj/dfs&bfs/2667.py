import sys

sys.setrecursionlimit(10 ** 8)
N = int(sys.stdin.readline())
graph = []
for i in range(N):
    graph.append(list(map(int,list(sys.stdin.readline().strip()))))


def dfs(start_node):
    i, j = start_node

    if i<0 or j<0 or i>=N or j>=N:
        return 0
    elif graph[i][j]==0:
        return 0
    elif graph[i][j]==1:
        graph[i][j]=0
        return 1 + dfs((i-1, j)) + dfs((i+1, j)) + dfs((i, j-1)) + dfs((i, j+1))

count = 0
result = []
for i in range(N):
    for j in range(N):
        a = dfs((i,j))
        if a:
            count += 1
            result.append(a)

print(count)
for r in sorted(result):
    print(r)