import sys

n = int(sys.stdin.readline())

if n%5==0:
    print(n//5)
elif n-3>0 and (n-3)%5==0:
    print(1+ (n-3)//5)
elif n-6>0 and (n-6)%5==0:
    print(2+(n-6)//5)
elif n-9>0 and (n-9)%5==0:
    print(3+(n-9)//5)
elif n-12>0 and (n-12)%5==0:
    print(4+(n-12)//5)

elif n%3==0:
    print(n//3)
else:
    print(-1)