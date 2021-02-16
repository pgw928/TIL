import sys
from collections import Counter
n, m = map(int, sys.stdin.readline().split())
A = sorted(map(int, sys.stdin.readline().split()))
cc = Counter(A)
print(cc)
check = {i:False for i in range(1,m+1)}
result = []
def sol(count):
    if len(list(cc))==1:
        result.append(tuple([1] * m))
        return
    for num in A:
        if count == m:
            # print(check, num, cc)
            # check[m] = num
            print(f'바로전 check:{check}')
            result.append(tuple(check.values()))
            return
        else:
            if cc[num] > 0:
                for j in range(1,m+1):
                    check[count+1], cc[num] = num, cc[num]-1
                    print(f'sol 들어가기 전, cc:{cc}, check:{check}')
                    sol(count+1)
                    check[count+1], cc[num] = False, cc[num]+1

sol(0)
result = sorted(list(set(result)))
for r in result:
    print(' '.join(map(str, r)))