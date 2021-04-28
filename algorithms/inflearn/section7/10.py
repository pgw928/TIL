import sys
sys.stdin = open('section7/input.txt', 'rt')

graph = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def dfs(node=(0, 0)):
    global cnt
    if node==(6, 6):
        cnt += 1
        return
    y, x = node 
    for k in range(4):
        b, a = y+dy[k], x+dx[k]
        if 0<=b<7 and 0<=a<7 and graph[b][a]==0:
            graph[b][a] = 1
            dfs((b, a))
            graph[b][a] = 0
graph[0][0] = 1
dfs()
print(cnt)