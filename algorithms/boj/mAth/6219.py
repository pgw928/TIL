import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())


def isprime2(a, b):
    A = [True]*(b+1)
    A[0], A[1] = False, False

    if b <= 3:
        return A
    i = 2
    while i*i<=b:
        for k in range(2*i,b+1,i):
            if A[k] == True:
                A[k] = False
        i += 1
    return A

A = isprime2(a, b)
for i in range(a,b+1):
    if A[i] == True:
        print(str(i))
        if f'{c}' not in str(i):
            A[i] = False

count = 0
for i in range(a,b+1):
    if A[i] == True:
        count += 1
print(A)
print(count)
