import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0
j = 0
l_A = len(A)
l_B = len(B)

result = [0]* (l_A+l_B)
while True:
    if A[i]< B[j]:
        result[i+j] = A[i]
        print(f'i:{i}, j:{j}, i+j:{i + j}, result:{result}')
        i += 1
    else:
        result[i+j] = B[j]
        print(f'i:{i}, j:{j}, i+j:{i + j}, result:{result}')
        j += 1
    print(f'i:{i}, j:{j}')
    if i==l_A:
        flag = True
        break
    elif j==l_B:
        flag = False
        break

if flag:
    for k in range(j,l_B):
        result[i+k] = B[k]
else:
    for k in range(i,l_A):
        result[j+k] = A[k]

print(' '.join(map(str,result)))