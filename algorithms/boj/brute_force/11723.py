import sys

input = sys.stdin.readline

M = int(input())


S = list()
for i in range(M):
    temp = input().split()
    op = temp[0]
    if len(temp)==2:
        num = int(temp[1])
    if op == 'add':
        if num not in S:
            S.append(num)
    elif op == 'remove':
        if num in S:
            S.remove(num)
    elif op == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if num in S:
            S.remove(num)
        else:
            S.append(num)
    elif op == 'all':
        S = list(range(1,21))
    elif op == 'empty':
        S = []
