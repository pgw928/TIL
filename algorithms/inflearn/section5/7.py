import sys
sys.stdin = open('section5/input.txt', 'rt')
necc = input().rstrip()
n = int(input())
for _ in range(n):
    s = input().rstrip()
    idx = 0
    flag = False
    for a in s:
        if necc[idx]==a:
            idx += 1
        elif a in necc[idx:]:
            break
        if idx==len(necc):
            flag = True
            break
    if flag:
        print('YES')
    else: print('NO')        