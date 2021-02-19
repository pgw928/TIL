import sys
a, b = map(int, sys.stdin.readline().split())

def is_square_nono(a, b):
    arr = list(range(a, b+1))
    k = 2
    while k*k<=b:
        continue_pt = True
        for j in range(1,a//k**2 +2):
            if j*k**2 >= a:
                arr[ j*k**2-a] = 0
                r = j*k**2
                continue_pt = False
                break
        if continue_pt:
            k += 1
            continue
        for val in range(2*r, b+1 ,k**2):
            arr[val-a] = 0

        k = k+2 if k>2 else k+1
    return len([True for num in arr if num>0])

print(is_square_nono(a, b))


