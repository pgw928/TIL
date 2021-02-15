import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(map(int, sys.stdin.readline().split()))
check = { i:None for i in range(1, m+1)}

def sol(count):
    for j in nums:
        if count == m:
            print(' '.join(tuple(map(str, check.values()))))
            return
        check[count+1] = j
        sol(count+1)
        check[count+1] = None

sol(0)