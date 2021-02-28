import sys
input = sys.stdin.readline
x, y = map(int, input().split())
print(y/x*100)

z = int(y*100/x)
if z >= 99:
    print(-1)
else:
    z += 1
    right = (x*z-100*y)/(100-z)
    if right == int(right):
        print(int(right))
    else:
        print(int(right)+1)