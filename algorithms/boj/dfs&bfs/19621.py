import sys

input =sys.stdin.readline
n = int(input())
graph = sorted([tuple(map(int, input().split())) for _ in range(n)])

def dfs(start, i):

    s, e, k = start
    check[i] = k
    for idx, (a, b, c) in enumerate(graph[i:],i):
        if a >= e:
            check[i] = max(dfs((a, b, c+k),idx), check[i])
    return check[i]

result = 0
check = [-1] * n
for i in range(n):
    result = max(dfs(graph[i], i), result)
print(result)