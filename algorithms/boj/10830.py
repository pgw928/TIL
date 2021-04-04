import sys; input = sys.stdin.readline
n, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def mat_square(graph):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        tmp1 = graph[i]
        for j in range(n):
            tmp2 = [graph[k][j] for k in range(n)]
            res[i][j] = sum([x*y for x,y in zip(tmp1, tmp2)])
    return res

def mat_product(mat1, mat2):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        tmp1 = mat1[i]
        for j in range(n):
            tmp2 = [mat2[k][j] for k in range(n)]
            res[i][j] = sum([x*y for x,y in zip(tmp1, tmp2)])
    return res
i = 2
while True:
    if b//i:
        i *=i
    else:
        i//=2
        break
print(i)




print(mat_square(graph))




