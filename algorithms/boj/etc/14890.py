import sys; input = sys.stdin.readline
n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
res = 0


for g in graph:
    check = [0]*n
    i = 0
    flag = True
    while i<n-1:
        if abs(g[i]-g[i+1])>1:
            flag = False
            break
        elif g[i]==g[i+1]:
            i += 1
        elif g[i]>g[i+1]: 
            if i+l>n-1:
                flag = False
                break
            if g[i+1:i+l+1] != [g[i+1]]*l:
                flag = False
                break
            else:
                check[i+1:i+l+1] = [1]*l
                i += l
        elif g[i]<g[i+1]:
            if i-(l-1) < 0:
                flag = False
                break
            if g[i-(l-1):i+1] != [g[i]]*l:
                flag = False
                break
            elif 1 in check[i-(l-1):i+1]:
                flag = False
                break
            else:
                i += 1
    if flag:
        res += 1               
 
for j in range(n):
    g = [graph[k][j] for k in range(n)]
    check = [0]*n
    i = 0
    flag = True
    while i<n-1:
        if abs(g[i]-g[i+1])>1:
            flag = False
            break
        elif g[i]==g[i+1]:
            i += 1
        elif g[i]>g[i+1]: 
            if i+l>n-1:
                flag = False
                break
            if g[i+1:i+l+1] != [g[i+1]]*l:
                flag = False
                break
            else:
                check[i+1:i+l+1] = [1]*l
                i += l
        elif g[i]<g[i+1]: 
            if i-(l-1) < 0:
                flag = False
                break
            if g[i-(l-1):i+1] != [g[i]]*l:
                flag = False
                break
            elif 1 in check[i-(l-1):i+1]:
                flag = False
                break
            else:
                i += 1
    if flag:
        res += 1               
 
print(res)