import sys; input = sys.stdin.readline

def is_prime(k):
    if k==1:
        return False
    j = 2
    while j*j<=k:
        if k%j ==0:
            return False
        j += 1
    return True

while True:
    n = int(input())
    if n==0:
        break
    for p in range(3,n-2):
        if is_prime(p) and is_prime(n-p):
            print(f'{n} = {p} + {n - p}')
            break