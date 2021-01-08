import sys

input = sys.stdin.readline

N = int(input())


def sol(st):
    if st[0]=='O':
        count = 1
    else:
        count = 0

    tmp = count
    for i, n in enumerate(st):
        if i==0:
            continue

        if n=='O':
            if st[i-1]=='O':
                tmp += 1
                count += tmp
            elif st[i-1]=='X':
                tmp = 1
                count += tmp
        else:
            tmp = 0
    return count

for _ in range(N):
    s = input().strip()
    print(sol(s))