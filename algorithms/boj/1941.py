import sys; input = sys.stdin.readline
graph = [input().rstrip() for _ in range(5)]

visited = {(i,j):[0, 0, 0, 0] for i in range(5) for j in range(5)}
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
res = []
def dfs(node, ss, yy, tmp):
    tmp1 = tmp
    y, x = node

    if ss+yy==7:
        set4tmp = set(tmp1)
        if set4tmp not in res:
            res.append(set4tmp)
        return
    for k in range(4):
        b, a = dy[k]+y, dx[k]+x
        if 0<=b<5 and 0<=a<5 and visited[(b,a)][k]==0:
            if sum(visited[(b,a)])!=0:
                visited[(b,a)][k] = 1
                dfs((b,a), ss, yy, (tmp1))
                visited[(b, a)][k] = 0
            elif graph[b][a] =='S':
                visited[(b,a)][k] = 1
                tmp1.append((b,a))
                dfs((b,a), ss+1, yy, (tmp1))
                tmp1.remove((b,a))
                visited[(b, a)][k] = 0
            elif yy+1<4:
                visited[(b, a)][k] = 1
                tmp1.append((b,a))
                dfs((b,a), ss, yy+1, (tmp1))
                tmp1.remove((b, a))
                visited[(b, a)][k] = 0

for i in range(5):
    for j in range(5):
        if graph[i][j]=='S':
            ss, yy = 1, 0
        else: ss, yy = 0, 1
        visited[(i, j)] = [1, 1, 1, 1]
        dfs((i, j), ss, yy, [(i, j)])
        visited[(i, j)] = [0, 0, 0, 0]
print(len(res))