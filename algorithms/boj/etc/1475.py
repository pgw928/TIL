import sys

num = sys.stdin.readline().strip()

dic = {f'{i}':0 for i in range(9)}

for s in num:
    if s=='9':
        dic['6'] += 1
    else:
        dic[s] += 1
q,r = divmod(dic['6'], 2)
dic['6'] = q + r

M = max(dic.values())
print(M)