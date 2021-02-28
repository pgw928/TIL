import sys

n, m, a = map(int, sys.stdin.readline().split())
q, r = divmod(a, m)
if r==0:
    r+=m
    q-=1

def sol(x, y):
    res = 1
    for i in range(y+1,x+y+1):
        res*=i
    for i in range(1,x+1):
        res//=i
    return res


if a==0 or a==n*m:
    print(sol(m-1,n-1))
else:
    print(sol(q,r-1)*sol(n-1-q, m-r))
