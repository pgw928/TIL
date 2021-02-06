import sys

input = sys.stdin.readline
t = int(input())

count = 0

for _ in range(t):
    break_pt = False
    st = list(input().strip())
    dic = {}
    for idx, s in enumerate(st):
        a = dic.get(s,0)
        if a:
            if st[idx-1]!=s:
                break_pt = True
                break
        else:
            dic[s] = a+1
    if not break_pt:
        count += 1
print(count)
