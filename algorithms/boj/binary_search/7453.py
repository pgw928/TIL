import sys

input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = sorted([a + b for a in A for b in B])
CD = sorted([c + d for c in C for d in D], reverse=True)

i, j = 0, 0
count = 0
l_AB, l_CD = len(AB), len(CD)
while (i < l_AB) and (j < l_CD):
    m = AB[i] + CD[j]
    if m == 0:
        a, b = 1, 1
        while True:
            if i + 1 < l_AB and AB[i] == AB[i + 1]:
                i += 1
                a += 1
            elif j + 1 < l_CD and CD[j] == CD[j + 1]:
                j += 1
                b += 1
            else:
                i += 1
                j += 1
                count += a*b
                break
    elif (m > 0):
        j += 1
    else:
        i += 1

print(count)