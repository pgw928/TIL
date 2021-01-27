import sys

input = sys.stdin.readline

N = int(input())
own = list(map(int, input().split()))
own.sort()

M = int(input())
cand = list(map(int, input().split()))
new = [[num, idx, 0] for idx, num in enumerate(cand)]
new.sort(key=lambda x: x[0])
i = len(own)-1
j = len(cand)-1


while i!=-1 and j!=-1:

    if own[i] > new[j][0]:
        i -= 1
    elif own[i] < new[j][0]:
        j -= 1
    else:
        new[j][2] = 1
        i -= 1
        j -= 1
new.sort(key=lambda x: x[1])

print(' '.join(map(str, [n[2] for n in new])))


