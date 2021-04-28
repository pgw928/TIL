import sys; input = sys.stdin.readline
from itertools import permutations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def count(k, idx):
    out, cnt = 3, 0
    r1, r2, r3 = 0, 0, 0 
    while out:
        idx %= 9
        if graph[k][order[idx]] == 0:
            out -= 1
            idx += 1
        elif graph[k][order[idx]] == 1:
            cnt += r3
            r1, r2, r3 = 1, r1, r2
            idx += 1
        elif graph[k][order[idx]] == 2:
            cnt += r2 + r3
            r1, r2, r3 = 0, 1, r1
            idx += 1
        elif graph[k][order[idx]] == 3:
            cnt += r1 + r2 + r3
            r1, r2, r3 = 0, 0, 1
            idx += 1
        elif graph[k][order[idx]] == 4: 
            cnt += 1 + r1 + r2 + r3
            r1, r2, r3 = 0, 0, 0
            idx += 1
    return cnt, idx


res = 0
perms = permutations(range(1,9),8)
for perm in perms:
    tmp = list(perm)
    order = tmp[0:3] + [0] + tmp[3:]
    l_res, idx = 0, 0
    for k in range(n):
        cnt, idx = count(k, idx)
        l_res += cnt
    res = max(res, l_res)
print(res)