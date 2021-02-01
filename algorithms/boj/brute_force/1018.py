import sys
from math import inf
input = sys.stdin.readline

N ,M = map(int, input().split())

graph = [list(input().strip()) for _ in range(N)]
m = inf

for i in range(N-8+1):
    r_chess = graph[i:i+9]
    for j in range(M-8+1):
        chess = [a[j:j+9] for a in r_chess]

        result1 = 0
        for i in range(8):
            for j in range(8):
                if ((i+j)%2==0) and chess[i][j]=='W':
                    result1 += 1
                elif ((i+j)%2==1) and chess[i][j]=='B':
                    result1 += 1
        m = min(result1, m)
        result2 =0
        for i in range(8):
            for j in range(8):
                if ((i+j)%2==0) and chess[i][j]=='B':
                    result2 += 1
                elif ((i+j)%2==1) and chess[i][j]=='W':
                    result2 += 1
        m = min(result2, m)
print(m)