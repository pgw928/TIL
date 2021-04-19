import sys
sys.stdin = open('section6/input.txt', 'rt')
n, m = map(int, input().split())
cnt = 0

def dfs(x):
    global cnt
    if x==m:
        print(visited)
        cnt += 1
        return
    for i in range(1, n+1):
        if all(i!=j for j in visited[:x]):
            visited[x] = i
            dfs(x+1)
            visited[x] = 0

visited = [0]*m
dfs(0)
print(cnt)