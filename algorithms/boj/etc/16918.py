import sys; input = sys.stdin.readline
r, c, n =map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

def find_bomb(g):
    bombs = []
    for i in range(r):
        for j in range(c):
            if g[i][j]=='O':
                bombs.append((i, j))
    return bombs

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
def bomb(bombs, g):
    for y, x in bombs:
        for k in range(4):
            b, a = y+dy[k], x+dx[k]
            if 0<=b<r and 0<=a<c and g[b][a]!='.':
                g[b][a]='.'
        g[y][x] = '.'
    return g




if n%2==0:
    for _ in range(r):
        print('O'*c)
else:
    k = 1
    while k!=n:
        bombs = find_bomb(graph)

        graph = [['O']*c for _ in range(r)]
        k+=1
        if k==n:
            break

        graph = bomb(bombs, graph)
        k += 1

    for g in graph:
        print(''.join(g))
