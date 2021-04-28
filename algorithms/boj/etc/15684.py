import sys; input = sys.stdin.readline
n, m, h = map(int, input().split())
edge = [[0]*(n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a][b] = 1

def check(start):
    c = start
    for i in range(1, h+1):
        if edge[i][c]==1:
            c += 1
        elif edge[i][c-1]==1:
            c -= 1
    if c == start:
        return True
    return False

def all_check():
    for i in range(1,n):
        if not check(i):
            return False
    return True
            
if all_check():
    print(0)
    sys.exit(0)

r = -1
for i1 in range(1, h+1):
    for j1 in range(1, n):
        if edge[i1][j1]==0 and edge[i1][j1-1]==0 and edge[i1][j1+1]==0:
            edge[i1][j1] = 1
            if all_check():
                print(1)
                sys.exit(0)
            if r==2:
                edge[i1][j1] = 0
                continue
            for i2 in range(1, h+1):
                for j2 in range(1, n):
                    if edge[i2][j2]==0 and edge[i2][j2-1]==0 and edge[i2][j2+1]==0:
                        edge[i2][j2] = 1
                        if all_check():
                            r = 2
                        if r>=2:
                            edge[i2][j2] = 0
                            continue
                        for i3 in range(1, h+1):
                            for j3 in range(1, n):
                                if edge[i3][j3]==0 and edge[i3][j3-1]==0 and edge[i3][j3+1]==0:
                                    edge[i3][j3] = 1
                                    if all_check():
                                        r = 3
                                    edge[i3][j3] = 0
                        edge[i2][j2] = 0
            edge[i1][j1] = 0
print(r)