import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [ list(map(int, input().strip())) for _ in range(N)]

check = [[ [0]*2 for _ in range(M)] for _ in range(N)]
check[0][0][0] = 1
# print(check)
# print(len(check))
# print(len(check[0]))
# print(len(check[0][0]))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(start_node):
    dq = deque()
    dq.append(start_node)

    while dq:
        print(dq)
        node = dq.popleft()
        y, x, i = node
        # if node[1:3] == end_node[1:3]:
        #     return min(check[y][x][0], check[y][x][1])
        for j in range(4):
            b = y + dy[j]
            a = x + dx[j]
            if 0<=b<N and 0<=a<M:
                if (i==1) and (check[b][a][i] == 0) and (graph[b][a] == 0):
                    print(f'이미 벽이 부서졌고{(y,x)}->{(b,a)} 이동중이예요')
                    check[b][a][1] = check[y][x][1] + 1
                    dq.append((b,a,1))
                elif (i==0) and (check[b][a][i] == 0):
                    if graph[b][a] == 0:
                        dq.append((b, a, 0))
                        check[b][a][0] = check[y][x][0] + 1
                        print(f'벽을 부순적 없고 {(y,x)}->{(b,a)} 벽이 없어서 이동해요')
                    elif graph[b][a] == 1:
                        dq.append((b, a, 1))
                        check[b][a][1] = check[y][x][0] + 1
                        print(f'벽을 부수고 {(y,x)}->{(b,a)} 이동해요')

bfs((0,0,0))
print(check)
if (check[N-1][M-1][0] == 0) and (check[N-1][M-1][1] == 0):
    print(-1)
elif check[N-1][M-1][0] == 0:
    print(check[N-1][M-1][1])
elif check[N-1][M-1][1] == 0:
    print(check[N - 1][M - 1][0])
else:
    print(min(check[N-1][M-1][1], check[N-1][M-1][0]))

