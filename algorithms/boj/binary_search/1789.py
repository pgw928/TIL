import sys
from math import ceil
a = int(sys.stdin.readline())
#---------------------------------
for i in range(a+1):
    result = int(i*(i+1)/2)
    if result > a :
        print(i-1 )
        break
#---------------------------------
if ceil((-1 + (1 + 8 * a) ** (1 / 2)) / 2) != int((-1 + (1 + 8 * a) ** (1 / 2)) / 2):
    print(ceil((-1 + (1 + 8 * a) ** (1 / 2)) / 2) - 1)
else:
    print(ceil((-1 + (1 + 8 * a) ** (1 / 2)) / 2))
