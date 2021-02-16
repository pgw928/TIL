import sys
input = sys.stdin.readline
n, m = map(int, input().split())
y, x, c = map(int, input().split())
check = [list(map(int, input().split())) for _ in range(n)] # 0:청소x, 1:벽, 2:청소o
rotate = {0:(0, -1, 3), 1:(-1, 0, 0) , 2:(0, 1, 1), 3:(1, 0, 2)} # 회전 시 방향 및 동서남북
back = {0:(1, 0), 1:(0, -1), 2:(-1,0), 3:(0, 1)} # 뒤로 갈 때 방향
check[y][x] = 2 # 첫 칸은 청소하고 시작
count = 1 # 청소하는 칸의 개수
while True:
    dy, dx, dc = rotate[c]
    b, a = dy+y, dx+x
    if check[b][a]==0:     # 조건 2-(a)
        y, x, c = b, a, dc
        check[b][a] = 2
        count += 1
    elif check[y+1][x]!=0 and check[y-1][x]!=0 and check[y][x-1]!=0 and check[y][x+1]!=0:
        dyy, dxx = back[c]
        u, v = dyy+y, dxx+x
        if check[u][v]!=1: # 조건 2-(c)
            y, x = u, v
        else:              # 조건 2-(d)
            break
    else:                  # 조건 2-(b)
        c = dc # 방향만 바꿈
print(count)