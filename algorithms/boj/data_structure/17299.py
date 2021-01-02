import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
count = Counter(A)
B = [count[i] for i in A]

result = ['-1' for _ in range(len(A))]
stack = []

for i in range(len(A)):

    while stack and B[stack[-1]] < B[i]:
        result[stack.pop()] = str(A[i])

    stack.append(i)

print(' '.join(result))
