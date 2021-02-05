import sys
N = int(sys.stdin.readline())

k = N-1
n = 2
count = 1
while k>=1 and n<N-2:
    temp = n*(2*k+n-1)//2
    if temp > N:
        k -= 1
    elif temp < N:
        n += 1
    elif temp==N:
        k -= 1
        n += 1
        count+= 1
    print(f'temp:{temp}, k:{k}, n:{n}, count:{count}')

print(count)