import sys; input = sys.stdin.readline
sys.setrecursionlimit(10_0000)

n, m , r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

l = min(n//2, m//2)
ravel  = []
for i in range(l):
    tmp = []
    tmp.extend(matrix[i][i:-1-i])
    tmp.extend([matrix[j][-i-1] for j in range(i, n-i-1)])
    tmp.extend(matrix[-1-i][i+1:m-i][::-1])
    tmp.extend([matrix[j][i] for j in range(i+1, n-i)][::-1])
    q = r%len(tmp)
    tmp = tmp[q:] + tmp[:q]
    ravel.extend(tmp)

rotate = [[0]*m for _ in range(n)]

dy, dx = [0,1,0,-1], [1,0,-1,0]
def dfs(start= (0, 0),idx=0,cur=0):
    y, x = start
    if rotate[y][x] == 0:
        rotate[y][x] = ravel[idx]

    b, a = y+dy[cur], x+dx[cur]
    if 0<=b<n and 0<=a<m and rotate[b][a]==0:
        dfs((b,a), idx+1, cur)
    else:
        if cur<3:
            cur += 1
            b, a = y + dy[cur], x + dx[cur]
            if 0 <= b < n and 0 <= a < m and rotate[b][a] == 0:
                dfs((b, a), idx + 1, cur)
        else:
            cur = 0
            b, a = y + dy[cur], x + dx[cur]
            if 0 <= b < n and 0 <= a < m and rotate[b][a] == 0:
                dfs((b, a), idx + 1, cur)

dfs()
for result in rotate:
    print(' '.join(tuple(map(str, result))))
