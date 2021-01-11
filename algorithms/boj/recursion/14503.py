import sys
sys.setrecursionlimit(8000)
input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

graph = [ list(map(int, input().split()))  for _ in range(N)]
check = [[0]*M for _ in range(N)]

# d : 0 => 북, 1 => 동, 2 => 남. 3 => 서
rotate  = [3, 0, 1, 2]
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

# 1 : 벽 , # 0 : 빈칸
# 지도의 첫행, 마지막 행, 첫 열, 마지막 열 : 모두 벽
start_node = (r, c, d)
def dfs(node):
    r, c, d = node
    # 1번
    if check[r][c] == 0:
        check[r][c] = 1
    print(check)
    # 2번
    n_r = r + dy[d]
    n_c = c + dx[d]
    n_d = rotate[d]

    if graph[r][c] == 1:
        return

    if (1<= n_r <=N-2) and (1<= n_c <=M-2):
        temp = {0, 1, 2, 3} - {d}
        # a
        if (graph[n_r][n_c]==0) and (check[n_r][n_c]==0):
            dfs((n_r, n_c, n_d))
        # b
        elif check[n_r][n_c] != 0 or graph[n_r][n_c] != 1:
            dfs((r , c, n_d))
        # d : 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.


        elif ((graph[r + dy[0]][c + dx[0]]==1 or
               check[r + dy[0]][c + dx[0]]==1) and
              (graph[r + dy[1]][c + dx[1]] == 1 or
               check[r + dy[1]][c + dx[1]] == 1) and
              (graph[r + dy[2]][c + dx[2]] == 1 or
               check[r + dy[2]][c + dx[2]] == 1) and
              (graph[r + dy[3]][c + dx[3]] == 1 or
               check[r + dy[3]][c + dx[3]] == 1)):

        # c
        elif ((graph[r + dy[0]][c + dx[0]]==1 or
               check[r + dy[0]][c + dx[0]]==1) and
              (graph[r + dy[1]][c + dx[1]] == 1 or
               check[r + dy[1]][c + dx[1]] == 1) and
              (graph[r + dy[2]][c + dx[2]] == 1 or
               check[r + dy[2]][c + dx[2]] == 1) and
              (graph[r + dy[3]][c + dx[3]] == 1 or
               check[r + dy[3]][c + dx[3]] == 1)):
            if d==0:
                dfs((r+1, c, d))
            elif d==1:
                dfs((r, c-1, d))
            elif d==2:
                dfs((r-1,c,d))
            elif d==3:
                dfs((r,c+1,d))


dfs(start_node)

print(check)
count = 0
for i in range(1,N):
    for j in range(1,M):
        if check[i][j]==1:
            count += 1

print(count)