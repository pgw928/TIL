import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

result = ['-1']*len(A)
stack = []
l = len(A)
for i, n in enumerate(A):
    while stack and (A[stack[-1]] < A[i]):
        print('res:',result, 'stack:',stack,'A:',A,'i:',i)
        result[stack.pop()] = str(A[i])

    stack.append(i)

print(' '.join(result))