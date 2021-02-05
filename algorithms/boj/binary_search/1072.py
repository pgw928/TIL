import sys
input = sys.stdin.readline
x, y = map(int, input().split())

i = 1
if 1+int(y/x*100)>=99:
    print(-1)
else:
    while True:

        if 1+int(y/x*100) == int((y+i)/(x+i)*100):
            print(i)
            break
        i+=1