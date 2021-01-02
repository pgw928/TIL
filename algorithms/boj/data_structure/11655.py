import sys
from collections import deque
input = sys.stdin.readline

stm = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'
beta = alpha[13:26] + alpha[0:13]

dct = {u:v for u,v  in zip(alpha,beta)}

result = ''
for s in stm:
    if s.islower():
        result +=dct[s]
    elif s == ' ':
        result += ' '
    elif s.isdecimal():
        result += s
    elif s.isupper():
        result += dct[s.lower()].upper()

print(result)