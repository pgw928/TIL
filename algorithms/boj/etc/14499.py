import sys
input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
order = tuple(map(int, input().split()))

direction = {1:(0, 1), 2:(0, -1), 3:(-1, 0), 4:(1, 0)}
dice = {'위':0, '밑':0, '왼':0, '오':0, '뒤':0, '앞':0}
def move(flag):
    if flag == 1:
        dice['위'], dice['왼'], dice['오'], dice['밑'] = dice['오'], dice['위'], dice['밑'], dice['왼']
    elif flag==2:
        dice['위'], dice['왼'], dice['오'], dice['밑'] = dice['왼'], dice['밑'], dice['위'], dice['오']
    elif flag == 3:
        dice['위'], dice['앞'], dice['밑'], dice['뒤'] = dice['뒤'], dice['위'], dice['앞'], dice['밑']
    elif flag == 4:
        dice['위'], dice['앞'], dice['밑'], dice['뒤'] = dice['앞'], dice['밑'], dice['뒤'], dice['위']


for i in range(k):
    dx, dy = direction[order[i]]
    a, b = dx+x, dy+y
    if a<0 or a>n-1 or b<0 or b>m-1:
        continue
    move(order[i])
    if graph[a][b]==0:
        graph[a][b] = dice['밑']
    else:
        dice['밑'] = graph[a][b]
        graph[a][b] = 0
    print(dice['위'])
    y, x = b, a