import sys; input = sys.stdin.readline
n, m = map(int, input().split())
graph= [list(map(int, input().split())) for _ in range(n)]

cctv1, cctv2, cctv3, cctv4, cctv5 = [], [], [], [], []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            cctv1.append((i,j))
        elif graph[i][j]==2:
            cctv2.append((i,j))
        elif graph[i][j]==3:
            cctv3.append((i,j))
        elif graph[i][j]==4:
            cctv4.append((i,j))
        elif graph[i][j]==5:
            cctv5.append((i,j))

dy, dx = [0 , 0, -1, 1], [1, -1, 0, 0]
def remove(camera,d):
    '''
    camera : coordinates
    d : direction
    '''
    y, x= camera
    b, a = y+dy[d], x+dx[d]
    while True:
        if b>=n or b<0 or a>=m or a<0 or graph[b][a]==6:
            break
        if graph[b][a] == 0:            
            graph[b][a] = -1
            b += dy[d]
            a += dx[d]
        else:
            b += dy[d]
            a += dx[d]
    # cctv5 는 지우고 시작:

for y, x in cctv5:
    for d in range(4):
        remove((y, x), d)

for g in graph:
    print(g)