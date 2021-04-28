import sys; input = sys.stdin.readline

coord = [(1, 1), (1, 3), (0, 4), (1, 5),
         (1, 7), (2, 6), (3, 7), (3, 5),
         (4, 4), (3, 3), (3, 1), (2, 2)]

graph = [list(input().rstrip()) for _ in range(5)]

alpha = [1 for i in range(65, 77)]
for y, x in coord:
    if graph[y][x]!='x':
        alpha[ord(graph[y][x])-65] = 0


res = []
def dfs(i):

    if i==5:
        if sum(map(ord, [graph[1][2*j+1] for j in range(4)]))-64*4!=26:
            return
    if i==7:
        if sum(map(ord, [graph[j][4+j] for j in range(4)]))-64*4!=26:
            return
    if i==9:
        if sum(map(ord, [graph[1+j][7-j] for j in range(4)]))-64*4!=26:
            return
    if i==11:
        if sum(map(ord, [graph[3][2*j+1] for j in range(4)])) - 64 * 4 != 26:
            return

    if i==11:
        for k in range(len(alpha)):
            if alpha[k] == 1:
                y, x = coord[i]
                if graph[y][x] == 'x':
                    graph[y][x] = chr(k+65)

                    res.append(graph)

    if i==11:
        if sum(map(ord, [graph[j][4-j] for j in range(4)]))-64*4!=26:
            return
        if sum(map(ord, [graph[1 + j][1 + j] for j in range(4)])) - 64 * 4 != 26:
            return
    if i==11:
        for g in graph:
            print(''.join(g))
        exit()

    else:
        for k in range(len(alpha)):
            if alpha[k]==1:
                y, x = coord[i]
                if graph[y][x]=='x':
                    graph[y][x] = chr(k + 65)
                    alpha[k] = 0
                    dfs(i+1)
                    graph[y][x] = 'x'
                    alpha[k] = 1
                else:
                    dfs(i+1)

dfs(0)