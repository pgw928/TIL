import sys

input = sys.stdin.readline

n = int(input())

u,v = map(int,input().split())

m = int(input())

lst = [ tuple(map(int,input().split())) for _ in range(m)]

graph = { i : [] for i in range(1,n+1)}
check = [0 for i in range(n+1)]
for t in lst:
    a,b = t
    graph[a].append(b)
    graph[b].append(a)

check[u]=1
def dfs(start_node):

    for i in graph[start_node]:
        if check[i] == 0:
            check[i] = check[start_node] + 1
            dfs(i)
dfs(u)

print(check[v]-1)