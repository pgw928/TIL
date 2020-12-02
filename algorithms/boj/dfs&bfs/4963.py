import sys
sys.setrecursionlimit(10000)
def dfs(start_node):

    x = start_node[0]
    y = start_node[1]
    if x<=-1 or y<=-1 or x>=h or y>=w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs([x - 1, y])
        dfs([x + 1, y])
        dfs([x, y - 1])
        dfs([x, y + 1])

        dfs([x+1, y + 1])
        dfs([x-1, y + 1])
        dfs([x+1, y - 1])
        dfs([x-1, y - 1])


        return True
    return False

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    count=0
    for i in range(h):
        for j in range(w):
            if dfs([i,j]):
                count += 1

    print(count)

