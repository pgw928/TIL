import sys; input = sys.stdin.readline
t = int(input())

def gcd(a, b):

    if b%a==0:
        return a
    return gcd(b%a, a)

for _ in range(t):
    A = tuple(map(int, input().split()))
    gcds = []
    for i in range(1,A[0]):
        for j in range(i+1, A[0]+1):
            gcds.append(gcd(A[i], A[j]))
    print(sum(gcds))