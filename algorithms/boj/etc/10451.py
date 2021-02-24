import sys
input = sys.stdin.readline
t = int(input())

def sol(n, permu):
    count = 0
    check = set()
    for i in range(n):
        if i+1 in check:
            continue
        count += 1
        while True:
            j = permu[i]
            if j in check:
                break
            check.add(j)
            i = j-1
    return count

for _ in range(t):
    n = int(input())
    permu = tuple(map(int, input().split()))
    print(sol(n, permu))