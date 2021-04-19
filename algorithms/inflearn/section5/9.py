import sys
sys.stdin = open('section5/input.txt', 'rt')

s1 = input().rstrip()
d1 = dict()
for s in s1:
    d1[s] = d1.get(s, 0) + 1

s2 = input().rstrip()
d2 = dict()
for s in s2:
    d2[s] = d2.get(s, 0) + 1

if d1==d2:
    print('YES')
else: print('NO')