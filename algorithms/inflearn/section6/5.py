import sys
sys.stdin = open('section6/input.txt', 'rt')
c, n = map(int, input().split())
arr = [int(input()) for _ in range(n)]
m = 0
total = sum(arr)
def dfs(node, s, mm):
    global m
    if s + (total- mm) < m:
        return
    if s > c:
        return
    if node == n-1:
        if s > m:
            m = s
        return

    if node+1 < n:
        dfs(node+1, s+arr[node+1], s+arr[node+1])
        dfs(node+1, s, s+arr[node+1])

dfs(0, 0, arr[0])
dfs(0, arr[0], arr[0])
print(m)