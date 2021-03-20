import sys; input = sys.stdin.readline
from itertools import permutations
from copy import deepcopy
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
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

def find_direction(i, j, g):
    counts = {0: 0, 1: 0, 2: 0, 3: 0}
    for k in range(4):
        y, x = dy[k] + i, dx[k] + j
        while True:
            if 0 <= y < n and 0 <= x < m:
                if g[y][x] == 6:
                    break
                elif g[y][x] == 0:
                    counts[k] += 1
                    y, x = y + dy[k], x + dx[k]
                else:
                    y, x = y + dy[k], x + dx[k]
                    continue
            else:
                break
    return counts

def monitor(i, j, domain, g):
    for k in domain:
        y, x = dy[k]+i, dx[k]+j
        while True:
            if 0<=y<n and 0<=x<m :
                if g[y][x]==6:
                    break
                elif g[y][x]==0:
                    g[y][x] = -1
                    y, x = y + dy[k], x + dx[k]
                else:
                    y, x = y + dy[k], x + dx[k]
                    continue
            else:
                break
    return g

def fuc_cctv4(g):
    if cctv4:
        m = 640
        perms = permutations(cctv4, len(cctv4))

        for perm in perms:
            gr = deepcopy(g)
            for i, j in perm:
                counts = find_direction(i, j, gr)
                domain = [a for a, b in sorted(list(counts.items()), reverse=True, key=lambda x: x[1])]
                n_g = monitor(i, j, domain[0:3], gr)
            tmp = sol(n_g)
            if tmp < m:
                result = deepcopy(n_g)
        return result
    return g

def fuc_cctv3(g):
    if cctv3:
        m = 640
        perms = permutations(cctv3, len(cctv3))
        for perm in perms:
            gr = deepcopy(g)
            for i, j in perm:
                counts = find_direction(i, j, gr)
                cri = [counts[0] + counts[1], counts[1] + counts[2], counts[2] + counts[3], counts[0]+counts[3]]
                if max(cri) == cri[0]:
                    n_g = monitor(i, j, [0, 1], gr)
                elif max(cri) == cri[1]:
                    n_g = monitor(i, j, [1, 2], gr)
                elif max(cri) == cri[2]:
                    n_g = monitor(i, j, [2, 3], gr)
                elif max(cri) == cri[3]:
                    n_g = monitor(i, j, [0, 3], gr)
            tmp = sol(n_g)
            if tmp < m:
                result = deepcopy(n_g)
        return result
    return g



def fuc_cctv2(g):
    if cctv2:
        m = 640
        perms = permutations(cctv2, len(cctv2))
        for perm in perms:
            gr = deepcopy(g)
            for i, j in perm:
                counts = find_direction(i, j, gr)
                cri = [counts[0] + counts[2], counts[1] + counts[3]]
                if max(cri) == cri[0]:
                    n_g = monitor(i, j, [0, 2], gr)
                elif max(cri) == cri[1]:
                    n_g = monitor(i, j, [1, 3], gr)
            tmp = sol(n_g)
            if tmp < m:
                result = deepcopy(n_g)
        return result
    return g


def fuc_cctv1(g):
    if cctv1:
        m = 640
        perms = permutations(cctv1, len(cctv1))
        for perm in perms:
            gr = deepcopy(g)
            for i, j in perm:
                counts = find_direction(i, j, gr)
                domain = [a for a, b in sorted(list(counts.items()), reverse=True, key=lambda x: x[1])]
                n_g = monitor(i, j, domain[0:1], gr)
            tmp = sol(n_g)
            if tmp < m:
                result = deepcopy(n_g)
        return result
    return g


def sol(g):
    count = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                count += 1
    return count


if cctv5:
    for i, j in cctv5:
        graph = monitor(i, j, range(4), graph)


funcs = [fuc_cctv1, fuc_cctv2, fuc_cctv3, fuc_cctv4]
M = 640
for perm in permutations(funcs, 4):
    g = deepcopy(graph)
    for func in perm:
        g = func(g)
    for gg in g:
        print(gg)
    print('--------')
    M = min(M, sol(g))
    print(M)

print(M)
