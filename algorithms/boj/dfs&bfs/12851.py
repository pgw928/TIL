import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
check = [100000]*100001
def bfs(start, end):
    dq = deque()
    dq.append((start, 0))
    check[start] = 0
    count = 0
    while dq:
        node, c = dq.popleft()
        if node == end and c<=check[node]:
            count += 1
            check[node] = c
            continue
        if node > end:
            if c+1 <= check[node-1]:
                dq.append((node-1, c+1))
                check[node-1] = c + 1

        else:
            for n_n in [node-1, node+1, 2*node]:
                if 0<= n_n<=100000 and c+1<=check[n_n]:
                    dq.append((n_n, c+1))
                    check[n_n] = c+1
    return check[end], count

res = bfs(n, m)
print(res[0])
print(res[1])