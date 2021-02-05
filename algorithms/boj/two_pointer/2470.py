import sys
from math import inf

input = sys.stdin.readline
n = int(input())
A = sorted(list(map(int, input().split())))

def binary_search(A):

    i = 0
    j = len(A)-1
    r = inf
    while i < j:
        tmp = A[i]+A[j]
        if tmp == 0:
            return A[i], A[j]

        if abs(tmp) < r:
            result = (A[i], A[j])
            r = abs(tmp)
        if tmp > 0:
            j -= 1
        else:
            i += 1
    return result

result = binary_search(A)
print(result[0], result[1])