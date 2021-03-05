import sys; input = sys.stdin.readline
n, m = map(int, input().split())
A = sorted(list(input().strip().split()))
print(A)
vowel = {s:0 for s in 'aeiou'}
consonant = {s:0 for s in 'bcdfghjklmnpqrstvwxyz'}
alpha = [0]*26
for a in A:
    alpha[ord(a)-ord('a')] = 1
print(alpha)

def dfs(s, i):

    if i==n-1:

    for j in range(i,m):
        if alpha[j] > 1:
            dfs(s+chr(j+ord('a')), j)