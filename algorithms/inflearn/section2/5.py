import sys
from collections import Counter
sys.stdin = open('section2/input.txt', 'rt')
n, m = map(int, input().split())
res = dict()
cnt = list(Counter([i + j for i in range(1,n+1) for j in range(1,m+1)]).items())
cnt.sort(key=lambda x:(-x[1],x[0] ))

rtn = [cnt[0]]
for i, j in cnt:
    if j==cnt[0][1]:
        rtn.append(i)
print(' '.join(list(map(str, rtn))))

