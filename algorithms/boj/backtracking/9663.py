import sys
n = int(sys.stdin.readline())

graph = {i:0 for i in range(n)}

def is_promising(v, w):
    i = 0
    while i<v:
        if abs(graph[i]-w)==v-i or graph[i]==w:
            return False
        i += 1
    return True

def n_queens(v,w):
    global count
    if is_promising(v, w):
        graph[v] = w
        if v==n-1:
            count += 1
            return
        for j in range(n):
            n_queens(v+1, j)


count = 0
for i in range(n):
    n_queens(0,i)
print(count)

#------------------------
import sys
n = int(sys.stdin.readline())
count = 0
vert, sla, bsla = [True]*n, [True]*(2*n-1), [True]*(2*n-1)

def sol(depth):
    global count
    if depth==n:
        count += 1
        return
    for j in range(n):
        if vert[j] and sla[j+depth] and bsla[n-j+depth-1]:
            vert[j], sla[j+depth], bsla[n-j+depth-1] = False, False, False
            sol(depth+1)
            vert[j], sla[j + depth], bsla[n - j + depth-1] = True, True, True

sol(0)
print(count)
