import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())

graph = [ list(map(int,input().split())) for _ in range(N)]

M = 0
for i in range(N):
    temp = Counter(graph[i])
    if 4 in temp.values():
        for k in temp.keys():
            M = max(M, 50000+5000*k)
    elif 3 in temp.values():
        for k in temp.keys():
            if temp[k]==3:
                M = max(M, 10000+1000*k)
    elif len(temp.values())==3:
        for k in temp.keys():
            if temp[k]==2:
                M = max(M, 1000 + 100 * k)
    elif len(temp.values())==2:
        M = max(M, 2000 + 500 * sum(map(lambda x:x,  temp.keys())))
    elif len(temp.values())==4:
        M = max(max(temp.keys())*100,M)
print(M)