import sys; input = sys.stdin.readline
p11, p12 = map(int, input().split())
p21, p22 = map(int, input().split())
p31, p32 = map(int, input().split())

if p11-p21 != 0:
    l1 = (p22-p12)/(p21-p11)
else:
    l1 = float('inf')
if p31-p21 != 0:
    l2 = (p32-p22)/(p31-p21)
else:
    l2 = float('inf')

if l1==l2:
    print(0)
elif p21-p11 > 0:
    if (p22-p12)*(p31-p11)/(p21-p11) + p12 < p32:
        print(1)
    elif (p22-p12)*(p31-p11)/(p21-p11) + p12 > p32:
        print(-1)
elif p21-p11 < 0:
    if (p22-p12)*(p31-p11)/(p21-p11) + p12 < p32:
        print(-1)
    elif (p22-p12)*(p31-p11)/(p21-p11) + p12 > p32:
        print(1)
elif p21-p11==0:
    if p31-p21>0:
        print(1)
    else:
        print(-1)

