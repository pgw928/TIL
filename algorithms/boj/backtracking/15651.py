import sys

n, m = map(int, sys.stdin.readline().split())
check = { i:None for i in range(1, m+1)}

def sol(count):
    for j in range(1, n+1):
        # if is_promising(check, j):
        if count == m:
            print(' '.join(tuple(map(str, check.values()))))
            return
        check[count+1] = j
        sol(count+1)
        check[count+1] = None


# def is_promising(check, j):
#     i = 1
#     while check[i]!=None and i<m:
#         if check[i]==j:
#             return False
#         i += 1
#     return True

sol(0)