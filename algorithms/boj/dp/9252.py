import sys; input = sys.stdin.readline
s1, s2 = input().strip(), input().strip()
l1 , l2 = len(s1) , len(s2)
A = [[0]*(l2+1) for i in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            A[i][j] = A[i-1][j-1]+1
        else:
            A[i][j] = max(A[i-1][j], A[i][j-1])
for a in A:
    print(a)

tmp = ''
j = l2
i = l1
while i>=1 and j>=1:
    if s1[i-1]==s2[j-1]:
        tmp += s1[i-1]
        i-=1
        j-=1
    elif A[i-1][j] > A[i][j-1]:
        i -= 1
    else:
        j -= 1
print(A[-1][-1])
print(tmp[::-1])