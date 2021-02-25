import sys
a, b = map(int, sys.stdin.readline().split())

def is_square_nono(a, b):
    arr = [1]*(b+1-a)
    k = 2
    while k*k<=b:
        start = (a//(k**2))*(k**2)
        if start<a:
            start += k*k
        for val in range(start, b+1 ,k**2):
            arr[val-a] = 0
        k= k+1 if k==2 else k+2

    return sum(arr)

print(is_square_nono(a, b))