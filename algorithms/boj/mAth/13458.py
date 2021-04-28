import sys; input = sys.stdin.readline
n = int(input())
people = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = 0
for i in range(n):
    p = people[i]
    if p <= b:
        cnt += 1
    else:
        p -= b
        cnt += 1
        if p%c==0:
            cnt += p//c
        else:
            cnt += p//c + 1
print(cnt)