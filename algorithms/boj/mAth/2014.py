import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = tuple(map(int, input().split()))

def sol(i):
    while True:
        flag = True
        if i == 1:
            return True
        for p in arr:
            if (i%p == 0):
                flag = False
                i //= p
        if flag:
            return False

result = 2
i = 2
j = 1
while j-1 != n:
    if sol(i):
        result = i
        j += 1
    i += 1

print(result)