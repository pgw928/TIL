import sys; input = sys.stdin.readline
sys.setrecursionlimit(10000)
n = int(input())
graph = [tuple(map(int, tuple(input().strip()))) for _ in range(n)]

def recursion(g):
    l = len(g)
    if l==1:
        return str(g[0][0])

    val = g[0][0]
    bk_pt = False
    for i in range(l):
        for j in range(l):
            if g[i][j]!=val:
                bk_pt = True
                break
        if bk_pt:
            break
    if not bk_pt:
        return f'{val}'
    res1 = recursion([g[i][:l//2] for i in range(l//2)])
    res2 = recursion([g[i][l//2:] for i in range(l//2)])
    res3 = recursion([g[i][:l//2] for i in range(l//2,l)])
    res4 = recursion([g[i][l//2:] for i in range(l//2,l)])
    return '(' + res1 + res2 + res3 + res4 + ')'

result = recursion(graph)
