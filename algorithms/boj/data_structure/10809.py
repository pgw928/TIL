import sys

input = sys.stdin.readline
word = list(input().strip())

alpha = 'abcdefghijklmnopqrstuvwxyz'

dict = {s : -1 for s in alpha}
for i, s in enumerate(word):
    if dict[s]==-1:
        dict[s] = i

print(' '.join(map(str,dict.values())))
