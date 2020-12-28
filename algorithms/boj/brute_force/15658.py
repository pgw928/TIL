import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

op_num = list(map(int, input().split()))
op = 'a'*op_num[0] + 'b'*op_num[1] + 'c'*op_num[2] + 'd'*op_num[3]
M, m = (0, 0)


for perm in permutations(op, len(A)-1):
    summation = A[0]
    for i in range(1,len(A)):
        if perm[i-1] == 'a':
            summation += A[i]
        elif perm[i-1] == 'b':
            summation -= A[i]
        elif perm[i-1] == 'c':
            summation *= A[i]
        elif perm[i-1] == 'd':
            if summation > 0:
                summation //= A[i]
            elif summation < 0:
                summation = -summation
                summation //= A[i]
                summation = -summation
    m = min(m, summation)
    M = max(M, summation)
print(M)
print(m)