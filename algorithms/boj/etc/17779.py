import sys; input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]



def count(x, y, d1, d2):
    
    r5 = 0
    for j in range(d2+1):
        r5 += sum([graph[x+i+j][y-i+j] for i in range(d1+1)])
    for j in range(d2):
        r5 += sum([graph[x+i+j+1][y-i+j] for i in range(d1)])

    r1 = 0
    for j in range(x+d1-1,-1,-1):
        if j < x:
            r1 += sum(graph[j][:y+1])
        else:
            r1 += sum(graph[j][:y-d1+1+(x+d1-1 - j)])
            
    r2 = 0
    for j in range(x+d2,-1,-1):
        if j <= x:
            r2 += sum(graph[j][y+1:])
        else:
            r2 += sum(graph[j][y+d2+1-(x+d2-j):])

    r3 = 0
    for j in range(x+d1,n):
        if j <= x+d1+d2:
            r3 += sum(graph[j][:y-d1+(j-x-d1)])
        else:
            r3 += sum(graph[j][:y-d1+d2])
        
    r4 = 0
    for j in range(x+d2+1, n):
        if x+d1+d2 < j:
            r4 += sum(graph[j][y-d1+d2:])
        else:
            r4 += sum(graph[j][y+d2+(x+d2+1 - j):])
        
    inf, sup = min(r1, r2, r3, r4, r5), max(r1, r2, r3, r4, r5)
    if x==1 and y==2 and d1==1 and d2==2:
        print(r1, r2, r3, r4,r5,f'x1:{x}, y1:{y}', d1, d2, sup-inf)
    return sup-inf
            
res = float('inf')
for x in range(n):
    for y in range(n):
        for d1 in range(1, n-x):
            for d2 in range(1,n-y):
                if 0<=x+d1+d2<n and 0<=y-d1 and y+d2<n:
                    res = min(res, count(x, y, d1, d2))
print(res)
                