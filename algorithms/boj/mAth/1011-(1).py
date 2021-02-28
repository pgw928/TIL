import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    s, e = map(int, input().split())
    n = e - s
    k = 1
    if n==1:
        print(1)
        continue
    while True:
        if k**2 < n <= k**2+k:
            print(2*k)
            break
        elif k**2+k< n <= (k+1)**2:
            print(2*k+1)
            break
        k+=1
