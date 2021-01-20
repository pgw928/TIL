import sys
from itertools import permutations
from math import inf

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, prod, divide = map(int, input().split())

perm = set(permutations([0]*plus + [1]*minus + [2]*prod + [3]*divide, n-1))
M = -inf
m = inf
for oper in perm:
    print(f'oper:{oper}')
    tmp = nums[0]
    for i in range(1,n):
        if oper[i-1] == 0:
            tmp += nums[i]
        elif oper[i-1] == 1:
            tmp -= nums[i]
        elif oper[i-1] == 2:
            tmp *= nums[i]
        else:
            if tmp<0:
                tmp = -((-tmp)//nums[i])
            else:
                tmp//=nums[i]
    print(f'temp:{tmp}')
    M = max(M, tmp)
    m = min(m, tmp)

print(M)
print(m)
