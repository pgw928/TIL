import sys

input = sys.stdin.readline
word = list(input().strip())

alpha = 'abcdefghijklmnopqrstuvwxyz'

dict = {s : 0 for s in alpha}
for s in word:
    dict[s]+=1

print(' '.join(map(str,dict.values())))
