import sys
import copy

sys.setrecursionlimit(8000)
N = int(sys.stdin.readline())

graph = []
for _ in range(N):
    temp = list(sys.stdin.readline().strip())
    graph.append(temp)

graph1 = copy.deepcopy(graph)
for i in range(N):
    for j in range(N):
        if graph1[i][j]=='R':
            graph1[i][j]='G'
print(graph)
print(graph1)

def dfs(grp, start_node, input_color):

    x, y = start_node
    if x<=-1 or y<=-1 or x>=N or y>=N:
        return False
    if grp[x][y] == 0:
        return False
    if grp[x][y]==input_color :
        grp[x][y] = 0
        dfs(grp, (x - 1, y), color)
        dfs(grp, (x + 1, y), color)
        dfs(grp, (x, y - 1), color)
        dfs(grp, (x, y + 1), color)
        return True
    return False



count = 0
count1 = 0
for i in range(N):
    for j in range(N):
        for color in ['R', 'G', 'B']:
            if dfs(graph, (i,j), color):
                count += 1

            if dfs(graph1, (i,j), color):
                count1 += 1
print(count, count1)