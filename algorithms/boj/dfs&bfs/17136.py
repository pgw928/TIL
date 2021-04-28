import sys; input = sys.stdin.readline
graph = [list(map(int, input().split())) for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
possible = [0]+[5]*5

def check(i, j, k):
    if i+k-1 >= 10 or j+k-1>= 10:
        return False
    tmp = []
    for y in range(i,i+k):
        for x in range(j, j+k):
            if graph[y][x]==0:
                return False
            else:
                tmp.append((y, x))
    return tmp

res = float('inf')
def dfs(idx, cnt):
    global res
    i, j = idx//10, idx%10
    if idx==99:
        if graph[i][j]==1:
            if possible[1]:
                res = min(res, cnt+1)    
                return
            else:
                return
        res = min(res, cnt)
        return
    if graph[i][j]==1:
        for k in range(1, 6):
            tmp = check(i, j, k) 
            if tmp and possible[k]:
                for (y, x) in tmp:
                    graph[y][x] = 0
                possible[k] -= 1
                dfs(idx+k, cnt + 1)
                possible[k] += 1
                for (y, x) in tmp:
                    graph[y][x] = 1
    else:
        dfs(idx+1, cnt)
dfs(0, 0)
if res==float('inf'):
    print(-1)
else:
    print(res)