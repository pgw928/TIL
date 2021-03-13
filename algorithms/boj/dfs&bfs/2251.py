import sys
from collections import deque
bottles = tuple(map(int, sys.stdin.readline().split()))

poss = {0:[1,2], 1:[0,2], 2:[0,1]}

def bfs():
    a, b, c = 0, 0, bottles[-1]
    dq, check = deque(), []
    dq.append([a, b, c])
    check.append([a,b,c])
    while dq:
        curr = dq.popleft()
        for idx, x in enumerate(curr):
            if x > 0:
                for n_idx in poss[idx]:
                    tmp = curr.copy()
                    able = bottles[n_idx] - curr[n_idx]
                    if x <= able:
                        tmp[idx] = 0
                        tmp[n_idx] = curr[n_idx] + x
                        if tmp not in check:
                            dq.append(tmp)
                            check.append(tmp)
                    else:
                        tmp[idx] = x-able
                        tmp[n_idx] = bottles[n_idx]
                        if tmp not in check:
                            dq.append(tmp)
                            check.append(tmp)
    print(check)
    return ' '.join(tuple(map(str, sorted(list(set([z for x,y,z in check if x==0]))))))

print(bfs())