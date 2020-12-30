import sys

input = sys.stdin.readline

N = int(input())

X = []

for _ in range(N):
    temp = input().split()
    if len(temp)>1:
        order, num = temp
    else:
        order = temp[0]
    if order == 'push':
        X.append(int(num))
    elif order == 'pop':
        if X:
            print(X.pop())
        else:
            print(-1)
    elif order == 'size':
        print(len(X))
    elif order == 'empty':
        if X:
            print(0)
        else:
            print(1)
    elif order == 'top':
        if X:
            print(X[-1])
        else:
            print(-1)



